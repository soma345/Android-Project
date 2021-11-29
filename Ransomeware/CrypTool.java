package com.example.myapplication;

import javax.crypto.Cipher;
import javax.crypto.NoSuchPaddingException;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.security.InvalidKeyException;
import java.security.Key;
import java.security.NoSuchAlgorithmException;

import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;
import javax.crypto.spec.SecretKeySpec;

public class CrypTool{

    public static final String ALGORITHM ="AES";
    public static final String TRANSFORMATION ="AES";

    public static void encrypt (String key, File inputFile , File outputFile) throws CryptoException{


        doCrypto(Cipher.ENCRYPT_MODE,key,inputFile,outputFile);
    }
    public static void decrypt (String key, File inputFile , File outputFile) throws CryptoException{

        doCrypto(Cipher.DECRYPT_MODE,key,inputFile,outputFile);
    }

    public static void doCrypto(int cipherMode, String key, File inputFile,
                                 File outputFile) throws CryptoException {

        Cipher cipher ;
        try {
            SecretKeySpec  secretKey = new SecretKeySpec(key.getBytes(), ALGORITHM);
            System.out.println("secretKey" +secretKey);
            cipher = Cipher.getInstance(TRANSFORMATION);
            System.out.println("cipher" +cipher);
            cipher.init(cipherMode,secretKey);
            System.out.println("secretKey" +secretKey);

            FileInputStream inputStream = new FileInputStream(inputFile);
            System.out.println("inputStream" +inputStream);
            byte[] inputBytes = new byte[(int) inputFile.length()];
            System.out.println("inputBytes" +inputBytes);
            inputStream.read(inputBytes);

            byte[] outputBytes = cipher.doFinal(inputBytes);
            System.out.println("outputBytes" +outputBytes);

            FileOutputStream outputStream = new FileOutputStream(outputFile);
            System.out.println("outputStream" +outputStream);
            outputStream.write(outputBytes);

            inputStream.close();
            outputStream.close();

        } catch (NoSuchPaddingException | NoSuchAlgorithmException | BadPaddingException | IllegalBlockSizeException | IOException | InvalidKeyException ex) {
            throw new CryptoException("Error encrypting/decrypting file", ex);
        }
    }
}

