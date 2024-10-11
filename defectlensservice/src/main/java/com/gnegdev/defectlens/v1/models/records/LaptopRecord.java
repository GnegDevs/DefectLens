package com.gnegdev.defectlens.v1.models.records;

public record LaptopRecord(
        int id,
        byte[] coverPhoto,
        byte[] screenPhoto,
        byte[] keyboardPhoto,
        byte[] basePhoto
) {
}
