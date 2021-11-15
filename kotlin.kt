import kotlin.math.sqrt

While loops - Find max
fun main() {
    var max = 0
    do {
        val num = readLine()!!.toInt()
        if (num > max) max = num
    } while (num != 0)
    println(max)
}


// While loops - The sum of elements
fun main() {
    var sum = 0
    do {
        val num = readLine()!!.toInt()
        sum += num
    } while (num != 0)
    println(sum)
}


 While loops - Collatz conjecture
fun main() {
    var num = readLine()!!.toInt()
    print("$num ")
    while (num != 1) {
        if (num % 2 == 0) num /= 2
        else num = 3 * num + 1
        print("$num ")
    }
}


 While loops - The sequence 1 2 2 3 3 3 ...
fun main() {
    val n = readLine()!!.toInt()
    var result = ""
    for (i in 1..(sqrt(2.0 * n.toDouble() + 1.0).toInt() + 1)) {
        repeat(i) { result += if (i * (i - 1) / 2 + it < n) "$i " else "" }
    }
    println(result)
}


fun main() {
    println(
        generateSequence(1) { it + 1 }
            .flatMap { i -> List(i) { i } }
            .take(readLine()!!.toInt())
            .toList()
            .joinToString(" ")
    )
}



// Oneliners
fun main() = repeat(1 + 1 + 1 + 1 + 1, { println("Kotlin") })


fun main() = println(if (readLine()!!.toInt() % 2 == 0) "EVEN" else "ODD")


fun main() = println(with(readLine()!!.toInt()) { if (this < 0) "negative" else if (this > 0) "positive" else "zero" })





// Size of parts
const val CATEGORIES = 3 // -1 = too small, 0 = perfect, 1 = too big
fun main() {
    val n = readLine()!!.toInt()
    val components = MutableList(CATEGORIES) { 0 }
    repeat(n) { components[readLine()!!.toInt() % 2 + 1] += 1 }
    println("${components[1]} ${components[2]} ${components[0]}")
}



// Leap Year
const val F = 4
const val OH = 100
const val FH = 400
fun main() {
    with(readLine()!!.toInt()) { println(if (this % F == 0 && this % OH != 0 || this % FH == 0) "Leap" else "Regular") }
}



// Balance Checker
fun main() {
    var balance = readLine()!!.toInt()
    val purchases = readLine()!!.split(" ").map { it.toInt() }
    var funds = true
    for (purchase in purchases) {
        if (balance - purchase < 0) {
            println("Error, insufficient funds for the purchase. Your balance is $balance, but you need $purchase.")
            funds = false
            break
        } else {
            balance -= purchase
        }
    }
    if (funds) {
        println("Thank you for choosing us to manage your account! Your balance is $balance.")
    }
}



// Initializing Mutable Lists
const val MAGIC_NUMBERS = "12 17 8 101 33"
fun main() {
    val numbers = MAGIC_NUMBERS.split(" ").map { it.toInt() }
    println(numbers.joinToString())
}


const val MAGIC_NUMBERS = "100_000_000_001 100_000_000_002 100_000_000_003"
fun main() {
    val longs = MAGIC_NUMBERS.split(" ").map { it.replace("_", "").toLong() }
    println(longs.joinToString())
}
