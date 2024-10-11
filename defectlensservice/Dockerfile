FROM openjdk:17
LABEL authors="ivanv"

ADD ./target/defectlens-0.0.1-SNAPSHOT.jar /usr/src/defectlens-0.0.1-SNAPSHOT.jar
WORKDIR usr/src
ENTRYPOINT ["java","-jar", "defectlens-0.0.1-SNAPSHOT.jar"]