object Fibonacci {

  def fib(n: Int): Int = {
    @annotation.tailrec
    def go(a: Int, b: Int, count: Int): Int = {
      count+=1
      var c=a+b
      a = b
      b = c
      if (count==n) c
      else go(a, b, count)
    }
    go(0, 1, 0)
  }

}