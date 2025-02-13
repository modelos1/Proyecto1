/*
 * This file has the definition of the user repositories for the digital wallet application.
 */
package com.example.digital_wallet.repositories;

import org.springframework.stereotype.Repository;
import java.util.Optional;
import java.util.List;
import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import com.example.digital_wallet.data_objects.*;
import org.json.JSONObject;
import org.json.JSONArray;

import jakarta.annotation.PostConstruct;

@Repository
public class UserRepositories {

    /*
     * 
     */
    private List<UserDAO> users = new ArrayList<UserDAO>();

    @PostConstruct
    public void init() {
        this.loadData();
    }
    /*
     * This method loads the data from the users.json file.
     */
    private void loadData() {
        String path = "data/users.json";
        try (InputStream is = getClass().getClassLoader().getResourceAsStream(path)) {
            if (is == null) {
                throw new FileNotFoundException("File not found: " + path);
            }
            String content = new String(is.readAllBytes(), StandardCharsets.UTF_8);
            JSONArray jsonArray = new JSONArray(content);
            for (int i = 0; i < jsonArray.length(); i++) {
                JSONObject jsonObject = jsonArray.getJSONObject(i);
                UserDAO user = new UserDAO(
                    jsonObject.getString("phone_number"),
                    jsonObject.getString("name"),
                    jsonObject.getString("email"),
                    jsonObject.getString("password"));
                this.users.add(user);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    /*
     * This method gets a user by its phone number.
     * @param phoneNumber The phone number of the user.
     * @return The user with the given phone number.
     */
    public Optional<UserDAO> getByPhoneNumber(String phoneNumber) {
        for (UserDAO user : this.users) {
            if (user.phone_number.equals(phoneNumber)) {
                return Optional.of(user);
            }
        }
        return Optional.empty();
    }
    /*
     * This method validates the user authentication.
     * @param authDTO The authentication data transfer object (DTO).
     * @return The user data transfer object (DTO) if the authentication is successful.
     */
    public Optional<UserDAO> login(AuthDTO authData) {
        for (UserDAO user : this.users) {
            if (user.phone_number.equals(authData.getPhone_number()) && user.password.equals(authData.getPassword())) {
                return Optional.of(user);
            }
        }
        return Optional.empty();
    }
    /*
     * This method creates a new user.
     * @param userDAO The user data access object (DAO).
     * @return The user data access object (DAO) created.
     */
    public Optional<UserDAO> create(UserDAO user) {
        if (this.getByPhoneNumber(user.phone_number).isPresent()) {
            return Optional.empty();
        }
        this.users.add(user);
        return Optional.of(user);
    }

}
