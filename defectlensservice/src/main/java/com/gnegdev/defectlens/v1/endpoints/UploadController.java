package com.gnegdev.defectlens.v1.endpoints;

import com.gnegdev.defectlens.v1.models.request.LaptopRecordRequest;
import com.gnegdev.defectlens.v1.services.db.DBRepository;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;

@RestController
@RequestMapping("defectlens/api/v1/upload")
public class UploadController {
    private final DBRepository dbRepository;
    public UploadController(DBRepository dbRepository) {
        this.dbRepository = dbRepository;
    }

    @GetMapping("/ping")
    @ResponseStatus(HttpStatus.OK)
    public String ping() {
        return "ok";
    }

    @PostMapping("/images")
    public ResponseEntity<String> uploadPhotos(
            @RequestParam(value = "cover_photo", required = false) MultipartFile coverPhoto,
            @RequestParam(value = "screen_photo", required = false) MultipartFile screenPhoto,
            @RequestParam(value = "keyboard_photo", required = false) MultipartFile keyboardPhoto,
            @RequestParam(value = "base_photo", required = false) MultipartFile basePhoto) {
        try {
            String response = savePhotosToDB(new LaptopRecordRequest(
                    (coverPhoto != null) ? coverPhoto.getBytes() : new byte[0],
                    (screenPhoto != null) ? screenPhoto.getBytes() : new byte[0],
                    (keyboardPhoto != null) ? keyboardPhoto.getBytes() : new byte[0],
                    (basePhoto != null) ? basePhoto.getBytes() : new byte[0]));
            return ResponseEntity.ok("Image uploaded successfully: " + response);
        } catch (IOException e) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("Error uploading image");
        }
    }
    private String savePhotosToDB(LaptopRecordRequest laptopRecordRequest) throws IOException {
        dbRepository.insertLaptopRecord(laptopRecordRequest);
        return "Photos uploaded successfully";
    }
}
