/*
 * This file has a data object class that represents the authentication data transfer object (DTO) for the digital wallet application.
 * 
 * Aurhor: Julian David Pulido CArreño <judpulidoc@usitrital.edu.co>
 */

package com.example.digital_wallet.data_objects;


/* This class represents the authentication data transfer object (DTO) for the digital wallet application.
*/
public class AuthDTO {
    private String phone_number;
    private String password;

    public AuthDTO(String phone_number, String password) {
        this.phone_number = phone_number;
        this.password = password;
    }
    
    /*
     * This method returns the phone number of the authentication data transfer object (DTO).
     */
    public String getPhone_number() {
        return this.phone_number;
    }

    /*
     * This method returns the password of the authentication data transfer object (DTO).
     */
    public String getPassword() {
        return this.password;
    }
}
