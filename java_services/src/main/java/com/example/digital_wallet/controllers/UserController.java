/*
 * This file has the definition of the user endpoints for the digital wallet application.
 * Author: mipapi <judpulidoc@udistrital.edu.co>
 * 
 */
package com.example.digital_wallet.controllers;

import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.digital_wallet.data_objects.AuthDTO;
import com.example.digital_wallet.data_objects.UserDAO;
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
    public ResponseEntity<?> login(@RequestBody AuthDTO authData) {
    Optional<UserDAO> user = userServices.login(authData);
        if (user.isPresent()) {
            return ResponseEntity.ok(user.get()); // Devuelve el usuario si lo encuentra
        } else {
            return ResponseEntity.status(401).body("Invalid credentials"); // Responde con 401 si no existe
        }
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
