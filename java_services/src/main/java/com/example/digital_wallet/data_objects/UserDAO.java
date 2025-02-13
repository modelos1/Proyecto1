/*
 * this file has a data object class that represents the user data access object (DAO) for the digital wallet application.
 * 
 * author: Julian David Pulido Carreño <judpulidoc@uditrital.edu.co>
 */

package com.example.digital_wallet.data_objects;

/*
 * This class represents the user data access object (DAO) for the digital wallet application.
 */
public class UserDAO {
    public String phone_number;
    public String name;
    public String email;
    public String password;

    public UserDAO(String phone_number, String name, String email, String password) {
        this.phone_number = phone_number;
        this.name = name;
        this.email = email;
        this.password = password;
    }
 }