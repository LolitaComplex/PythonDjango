import java.io.*


fun main(args: Array<String>) {
    var fileSurce = File("Source.txt")
    var fileTarget = File("Target.txt")
    InputStreamReader(FileInputStream(fileSurce), "utf-8").buffered(1024 * 8).use { reader ->
        OutputStreamWriter(FileOutputStream(fileTarget), "utf-8").buffered(1024 * 8).use { writer->
            var line = ""
            while (reader.readLine().let { line = it; it != null}) {
                var newLine = line.replaceFirst("\\s+".toRegex(), "|`")
                newLine = newLine.replaceFirst("\\s+".toRegex(), "`|")
                println("| ${newLine} |")
                writer.write("| ${newLine} |" + "\n")
                writer.flush()
            }

        }
    }
    println(args)
}