package com.example.myapplication;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.FilenameFilter;
import java.io.IOException;

public class FileOperations {

    public boolean writeToFilesystem(String nameString, String contentString) throws IOException {
        //Not a successful write
        File f = new File("/sdcard/Download/"+nameString);

        if(!f.exists()){
            f.createNewFile();
        }

        FileWriter fw = new FileWriter(f.getAbsoluteFile());
        BufferedWriter bw = new BufferedWriter(fw);
        bw.write(contentString);
        bw.close();
        return true;

    }

    public String readFilesystem(String nameString) throws IOException {
        //Not a successful write
        String path = "/sdcard/Download/"+nameString;
        File f = new File(path);

        BufferedReader br= new BufferedReader(new FileReader(path));
        String line = br.readLine();
        return line;

    }


}
