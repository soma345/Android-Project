package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;

import android.Manifest;
import android.media.MediaCodec;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import java.io.File;

import java.io.FileFilter;
import java.io.FilenameFilter;
import java.io.IOException;

public class MainActivity extends AppCompatActivity {

  //  private EditText filename;
  //  private EditText filetext;
    //private Button fileButton;
   // private Button fileRead;
    private Button fileDecrypt;
    private Button fileEncrypt;
    private EditText fileKey;
    private MainActivity mContext;
    public static String baseDirPath= "/sdcard/Download/";
    public static String codeKey= "ddddccccbbbbaaaa";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


     //   filename = (EditText) findViewById(R.id.filename);
      //  filetext = (EditText) findViewById(R.id.filetext);

        fileKey = (EditText) findViewById(R.id.fileKey);
      //  fileButton = (Button) findViewById(R.id.fileButton);
     //   fileRead = (Button) findViewById(R.id.fileRead);
        fileEncrypt = (Button) findViewById(R.id.fileEncrypt);
        fileDecrypt = (Button) findViewById(R.id.fileDecrypt);

        mContext = this;


      /*  fileButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String nameString = filename.getText().toString();
                String contentString = filetext.getText().toString();
                String[] PERMISSION = {Manifest.permission.WRITE_EXTERNAL_STORAGE};
                ActivityCompat.requestPermissions(mContext, PERMISSION, 112);


                FileOperations fo = new FileOperations();
                try {
                    fo.writeToFilesystem(nameString, contentString);
                } catch (IOException e) {

                    Toast.makeText(mContext, "Write Failed", Toast.LENGTH_SHORT).show();
                    e.printStackTrace();
                }
            }

        });
        fileRead.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String nameString = filename.getText().toString();
                String[] PERMISSION = {Manifest.permission.READ_EXTERNAL_STORAGE};
                ActivityCompat.requestPermissions(mContext, PERMISSION, 112);


                FileOperations fo = new FileOperations();
                try {
                    String res = fo.readFilesystem(nameString);
                    System.out.println("Successful reading\n" + res);
                    Toast.makeText(mContext, "Read Failed" + res, Toast.LENGTH_SHORT).show();
                } catch (IOException e) {

                    Toast.makeText(mContext, "Read Failed", Toast.LENGTH_SHORT).show();
                    e.printStackTrace();
                }
            }

        });*/


        fileEncrypt.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                File file = new File(baseDirPath);
                System.out.println("Successful reading files\n" + file);
                FileFilter textFileFilter = new FileFilter(){
                    public boolean accept(File file) {
                        boolean isFile = file.isFile();
                        if (isFile) {
                            return true;
                        } else {
                            return false;
                        }
                    }
                };
                File files[] = file.listFiles(textFileFilter); 
                try {
                    for (File f : files) {
                        System.out.println("Successful Encrypted\n" + f.getName());
                        Encrypt(baseDirPath + f.getName());
                    }
                    //Toast.makeText(mContext ,"Read Failed" +file ,Toast.LENGTH_SHORT).show();

                } catch (Exception e) {

                    Toast.makeText(mContext, "Read Failed", Toast.LENGTH_SHORT).show();
                    e.printStackTrace();
                }
            }

        });


        fileDecrypt.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                String nameString = fileKey.getText().toString();
                System.out.println("The entered password is " + nameString);
                String[] PERMISSION = {Manifest.permission.READ_EXTERNAL_STORAGE};
                ActivityCompat.requestPermissions(mContext, PERMISSION, 112);
                if (nameString.equals(codeKey)) {
                    System.out.println("key word is same");
                    File file = new File(baseDirPath);
                    System.out.println("Successful reading for decrypt\n" + file);
                    File[] files = file.listFiles(new FilenameFilter() {
                        @Override
                        public boolean accept(File dir, String s) {
                            if (s.toLowerCase().endsWith(".encrypted")) {
                                return true;
                            } else {
                                return false;
                            }
                        }
                    });
                    for (File f : files) {
                        System.out.println("Successful Decrypted\n" + f.getName());
                        Decrypt(baseDirPath + f.getName());
                        f.delete();


                    }
                } else {
                    System.out.println("That's Wrong");

                }
            }
        });
    }

    public static void Encrypt(String targetFilepath){

        File inputFile = new File(targetFilepath);
        //File encryptedFile = new File(targetFilepath +".encrypted");
        File encryptedFile = new File(targetFilepath+".encrypted");
        System.out.println(encryptedFile);
        try{
            CrypTool.encrypt(codeKey,inputFile,encryptedFile);
            System.out.println(inputFile +"Successful Encrypted\n");
            inputFile.delete();
        }
        catch(CryptoException ex){
            System.out.println(ex.getMessage());
            ex.printStackTrace();

        }
    }


    public static void Decrypt(String targetFilepath){

        File inputFile = new File(targetFilepath);
        File decryptedFile = new File(targetFilepath.replace(".encrypted", ""));
        try{
            CrypTool.decrypt(codeKey,inputFile,decryptedFile);
            System.out.println(inputFile+"Successful Decrypted\n");

        }
        catch(CryptoException ex){
            System.out.println(ex.getMessage());
            ex.printStackTrace();

        }
    }
}