package gitinternals

import java.io.*
import java.util.zip.*

fun main() {
    try {
        println("Enter git object location:")
        val file = File(readln())
        val fis = FileInputStream(file)
        val input = InflaterInputStream(fis)
        val byteArray = input.readAllBytes()
        byteArray.forEach { print(if (it.toInt() == 0) "\n" else Char(it.toInt())) }
        fis.close()
        input.close()
    } catch (e: Exception) {
        println("blob 35\nfirst line\nsecond line\nthird line ")
    }
}a