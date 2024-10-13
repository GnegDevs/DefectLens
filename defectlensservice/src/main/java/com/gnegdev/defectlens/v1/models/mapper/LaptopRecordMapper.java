package com.gnegdev.defectlens.v1.models.mapper;

import com.gnegdev.defectlens.v1.models.records.LaptopRecord;
import org.springframework.jdbc.core.RowMapper;

import java.sql.ResultSet;
import java.sql.SQLException;
import org.springframework.stereotype.Component;

@Component
public class LaptopRecordMapper implements RowMapper<LaptopRecord> {

    @Override
    public LaptopRecord mapRow(ResultSet rs, int rowNum) throws SQLException {
        return new LaptopRecord(
                rs.getInt("id"),
                rs.getBytes("cover_photo"),
                rs.getBytes("screen_photo"),
                rs.getBytes("keyboard_photo"),
                rs.getBytes("base_photo"),
                rs.getString("serial")
        );
    }
}
