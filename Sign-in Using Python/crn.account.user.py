def mkdir():
    import os
    write = "iuere37389gg73896242"
    os.mkdir("C:/Users/Public/.account")
    os_write = open("C:\\Users\\Public\\.account\\.username.bin", "w")
    os_write.write(write)
    os_write.close()
    os_write1 = open("C:\\Users\\Public\\.account\\.password.bin", "w")
    os_write1.write(write)
    os_write1.close()
    os_write2 = open("C:\\Users\\Public\\.account\\1-2-1.bin", "w")
    os_write2.write(write)
    os_write2.close()

mkdir()