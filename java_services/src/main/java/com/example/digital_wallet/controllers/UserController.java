/*
 * This file has the definition of the user endpoints for the digital wallet application.
 * Author: Julian David Pulido Carreño <judpulidoc@udistrital.edu.co>
 * 
 */
package com.example.digital_wallet.controllers;

import java.util.Optional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import com.example.digital_wallet.data_objects.*;
import com.example.digital_wallet.services.UserServices;

@RestController
@RequestMapping("v1/users")
public class UserController {
    @Autowired
    private UserServices userServices;

    /*
     * This method gets a user by its phone number.
     * @param phoneNumber The phone number of the user.
     * @return The user with the given phone number.
     */
    @GetMapping("/get_by_phoneNumber/{phoneNumber}")
    public Optional<UserDAO> getByPhoneNumber(@PathVariable("phoneNumber") String phoneNumber) {
        return userServices.getByPhoneNumber(phoneNumber);
    }
    /*
     * this method validates the user authentication.
     * @param authDTO The authentication data transfer object (DTO).
     * @return The user data transfer object (DTO) if the authentication is successful.
     */
    @PostMapping("/login")
    public Optional<UserDAO> login(@RequestBody AuthDTO authData) {
        return userServices.login(authData);
    }
    /*
     * This method creates a new user.
     * @param userDAO The user data access object (DAO).
     * @return The user data access object (DAO) created.
     */
    @PostMapping("/create")
    public Optional<UserDAO> create(@RequestBody UserDAO user) {
        return userServices.create(user);
    }
    

}
