package com.gnegdev.defectlens.v1.services.db;

import com.gnegdev.defectlens.v1.models.mapper.LaptopRecordMapper;
import com.gnegdev.defectlens.v1.models.records.LaptopRecord;
import com.gnegdev.defectlens.v1.models.request.LaptopRecordRequest;
import org.springframework.jdbc.core.namedparam.MapSqlParameterSource;
import org.springframework.jdbc.core.namedparam.NamedParameterJdbcTemplate;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public class DBRepository {

    private static final String SQL_GET_LAPTOP_RECORD_BY_ID =
            "select id, cover_photo, screen_photo, keyboard_photo, base_photo from laptop_record where id = :id";
    private static final String SQL_INSERT_LAPTOP_RECORD =
            "insert into laptop_record (cover_photo, screen_photo, keyboard_photo, base_photo) values (:cover_photo, :screen_photo, :keyboard_photo, :base_photo)";


    private final LaptopRecordMapper laptopRecordMapper;
    private final NamedParameterJdbcTemplate jdbcTemplate;

    public DBRepository(
            LaptopRecordMapper eventMapper,
            NamedParameterJdbcTemplate jdbcTemplate
    ) {
        this.laptopRecordMapper = eventMapper;
        this.jdbcTemplate = jdbcTemplate;
    }

    public Optional<LaptopRecord> getLaptopRecordById(int id) {
        var params = new MapSqlParameterSource();
        params.addValue("id", id);
        return jdbcTemplate.query(
                        SQL_GET_LAPTOP_RECORD_BY_ID,
                        params,
                        laptopRecordMapper
                ).stream()
                .findFirst();
    }
    public void insertLaptopRecord(LaptopRecordRequest laptopRecordRequest) {
        var params = new MapSqlParameterSource();
        params.addValue("cover_photo", laptopRecordRequest.coverPhoto());
        params.addValue("screen_photo", laptopRecordRequest.screenPhoto());
        params.addValue("keyboard_photo", laptopRecordRequest.keyboardPhoto());
        params.addValue("base_photo", laptopRecordRequest.basePhoto());
        jdbcTemplate.update(SQL_INSERT_LAPTOP_RECORD, params);
    }
}
