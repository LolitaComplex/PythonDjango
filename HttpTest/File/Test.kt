
// 原方法
val sleep = { 
    println("执行逻辑......")
    Thread.sleep(1000) 
    println("=====================\n")
}

// 装饰方法
fun decorator(func: () -> Any) : () -> Unit{
    val inner = fun(){
        clacFuncTime(func)
    }
    return inner
}

// 装饰逻辑实现体
fun clacFuncTime(func: () -> Any){
    val start = System.currentTimeMillis()
    func.invoke()
    val end = System.currentTimeMillis()
    print("总时间：${end - start}")
}

fun main(args: Array<String>) {
    sleep();

    val sleep = decorator(sleep)
    sleep()
}




