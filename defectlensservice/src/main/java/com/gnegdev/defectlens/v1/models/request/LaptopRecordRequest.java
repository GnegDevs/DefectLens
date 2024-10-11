package com.gnegdev.defectlens.v1.models.request;

public record LaptopRecordRequest(
        byte[] coverPhoto,
        byte[] screenPhoto,
        byte[] keyboardPhoto,
        byte[] basePhoto
) {
}
