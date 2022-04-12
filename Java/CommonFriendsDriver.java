import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;

import java.io.IOException;
import java.util.*;

public class CommonFriendsDriver {
    public static class CommonFriendsMapper extends Mapper<LongWritable,Text,Text,Text> {
        static String getFriends(String[] tokens){
            if(tokens.length==2) return "";
            StringBuilder builder=new StringBuilder();
            for(int i=1;i<tokens.length;i++){
                builder.append(tokens[i]);
                if(i<(tokens.length-1)){
                    builder.append(",");
                }
            }
            return builder.toString();
        }
        static String buildSortedKey(String person,String friend){
            long p=Long.parseLong(person);
            long f=Long.parseLong(friend);
            if(p<f){
                return person+","+friend;
            }else{
                return friend+","+person;
            }
        }
        public void map(LongWritable key,Text value,Context context) throws IOException,InterruptedException{
            String[] tokens=value.toString().split(" ");
            String friends=getFriends(tokens);
            String person=tokens[0];
            for(int i=1;i<tokens.length;i++){
                String friend=tokens[i];
                String reduceKeyAsString=buildSortedKey(person,friend);
                context.write(new Text(reduceKeyAsString),new Text(friends));
            }
        }
    }
    public static class CommonFriendsReducer extends Reducer<Text,Text,Text,Text> {
        public void reduce(Text key,Iterable<Text> values,Context context) throws IOException,InterruptedException{
            Map<String,Integer> map=new HashMap<String,Integer>();
            Iterator<Text> iterator=values.iterator();
            int numOfValues=0;
            while(iterator.hasNext()){
                String friends=iterator.next().toString();
                if(friends.equals("")){
                    context.write(new Text("Friend"+key+"'s mutual friend is "),new Text("[]"));
                    return;
                }
                addFriends(map,friends);
                numOfValues++;
            }
            List<String> commonFriends=new ArrayList<String>();
            for(Map.Entry<String,Integer> entry:map.entrySet()){
                if(entry.getValue()==numOfValues){
                    commonFriends.add(entry.getKey());
                }
            }
            context.write(new Text("Friend"+key+"'s common friend is "),new Text(commonFriends.toString()));
        }
        static void addFriends(Map<String,Integer> map,String friendsList){
            String[] friends=friendsList.split(",");
            for(String friend:friends){
                Integer count=map.get(friend);
                if(count==null){
                    map.put(friend,1);
                }else{
                    map.put(friend,++count);
                }
            }
        }
    }
    public static void main(String[] args) throws Exception{
        Configuration conf=new Configuration();
        String[] otherArgs=new String[]{"/input/CommonFriends.txt","/output"};
        if(otherArgs.length!=2){
            System.err.println("entry error");
            System.exit(2);
        }
        Job job=new Job(conf,"CommonFriendsDriver");
        FileInputFormat.addInputPath(job,new Path(otherArgs[0]));
        FileOutputFormat.setOutputPath(job,new Path(otherArgs[1]));
        job.setJarByClass(CommonFriendsDriver.class);
        job.setMapperClass(CommonFriendsMapper.class);
        job.setReducerClass(CommonFriendsReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(Text.class);
        System.exit(job.waitForCompletion(true)?0:1);
    }
}

