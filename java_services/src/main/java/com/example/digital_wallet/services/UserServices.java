/*
 * This file has the definition of the business logic for the user services of the digital wallet application.
 * 
 * Author: Julian David Pulido Carreño <judpulidoc@udistrital.edu.co>
 */
package com.example.digital_wallet.services;
import java.util.Optional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.example.digital_wallet.repositories.UserRepositories;
import com.example.digital_wallet.data_objects.*;

@Service
public class UserServices {
    
    @Autowired
    public UserRepositories userRepositories;

    /*
     * This method gets a user by its phone number.
     * @param phoneNumber The phone number of the user.
     * @return The user with the given phone number.
     */
    public Optional<UserDAO> getByPhoneNumber(String phoneNumber) {
        if (phoneNumber == null || phoneNumber.length()+1 < 10) {
            return Optional.empty();
        }   
        return userRepositories.getByPhoneNumber(phoneNumber);
    }
    /*
     * This method validates the user authentication.
     * @param authDTO The authentication data transfer object (DTO).
     * @return The user data transfer object (DTO) if the authentication is successful.
     */
    public Optional<UserDAO> login(AuthDTO authData) {
        if (authData == null || authData.getPhone_number() == null || authData.getPassword() == null) {
            return Optional.empty();
        }
        return userRepositories.login(authData);
    }
    /*
     * This method creates a new user.
     * @param userDAO The user data access object (DAO).
     * @return The user data access object (DAO) created.
     */
    public Optional<UserDAO> create(UserDAO user) {
        if (user == null || user.phone_number == null || user.name == null || user.email == null || user.password == null || user.phone_number.length() < 10) {
            return Optional.empty();
        }
        return userRepositories.create(user);
}
    





}
