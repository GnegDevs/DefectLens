package com.gnegdev.defectlens.v1.endpoints;

import com.gnegdev.defectlens.v1.models.records.LaptopRecord;
import com.gnegdev.defectlens.v1.services.db.DBRepository;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Optional;

@RestController
@RequestMapping("defectlens/api/v1/record")
public class RecordsController {
    private final DBRepository dbRepository;
    public RecordsController(DBRepository dbRepository) {
        this.dbRepository = dbRepository;
    }

    @GetMapping("/ping")
    @ResponseStatus(HttpStatus.OK)
    public String ping() {
        return "ok";
    }

    @GetMapping("/{id}")
    @ResponseBody
    public ResponseEntity<Object> getEventById(@PathVariable int id) {
        Optional<LaptopRecord> event = dbRepository.getLaptopRecordById(id);
        if (event.isEmpty()) {
            return ResponseEntity.status(HttpStatus.NOT_FOUND).body("Event with id = " + id + " not found");
        }
        return ResponseEntity.status(HttpStatus.OK).body(event);
    }
}
