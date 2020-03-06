package com.example.myapplication.Activities;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import com.example.myapplication.R;
import com.google.gson.Gson;

public class RememberActivity extends AppCompatActivity {
    ConfigManager cfgManager;
    Button btn_menu;

    @Override
    protected void onStart() {
        super.onStart();

        ConfigManager.permissionCheck(this);   //Запрашиваем права

    }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_remember);
        Gson gson = new Gson();

        cfgManager = new ConfigManager(this, gson.toJson(new Result(1, "C", 1, "M", 0F, 1, 1)), "somefile");  //Создаём конфиг
        btn_menu = findViewById(R.id.btn_menu);

        btn_menu.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                startActivity(new Intent(RememberActivity.this, MenuActivity.class));

            }
        });
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions,
                                           @NonNull int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);

        ConfigManager.onRequestPermissionsResult(this, requestCode, grantResults);   //Получаем резхультат проверки прав

    }


}