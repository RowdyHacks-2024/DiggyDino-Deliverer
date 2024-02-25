DROP TABLE IF EXISTS Users;
CREATE TABLE Users (

    UserID TEXT NOT NULL PRIMARY KEY,
    Email TEXT NOT NULL

);

DROP TABLE IF EXISTS Detectors;
CREATE TABLE Detectors (

    DetectorID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    DetectorName TEXT NOT NULL,

    UserID TEXT NOT NULL,
    FOREIGN KEY (UserID) REFERENCES Users (UserID) ON DELETE CASCADE

);

DROP TABLE IF EXISTS Predictions;
CREATE TABLE Predictions (

    PredictionID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    IsValid INTEGER NOT NULL,

    UserID TEXT NOT NULL,
    FOREIGN KEY (UserID) REFERENCES Users (UserID) ON DELETE CASCADE

);

DROP TABLE IF EXISTS Samples;
CREATE TABLE Samples (

    SampleID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Longitude REAL NOT NULL,
    Latitude REAL NOT NULL,
    Temperature REAL NOT NULL,
    BarametricPressure REAL NOT NULL,
    Altitude REAL NOT NULL,

    UserID TEXT NOT NULL,
    FOREIGN KEY (USERID) REFERENCES Users (UserID) ON DELETE CASCADE

);
