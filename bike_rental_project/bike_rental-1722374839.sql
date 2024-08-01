CREATE TABLE IF NOT EXISTS "trips" (
	"id" bigint GENERATED ALWAYS AS IDENTITY NOT NULL UNIQUE,
	"trip_duration" bigint NOT NULL,
	"start_time" text NOT NULL,
	"stop_time" text NOT NULL,
	"start_station_id" bigint NOT NULL,
	"end_station_id" bigint NOT NULL,
	"bike_id" bigint NOT NULL,
	"user_type" text NOT NULL,
	"birth_year" bigint NOT NULL,
	"gender" bigint NOT NULL,
	PRIMARY KEY ("id"),
	FOREIGN KEY (start_station_id) REFERENCES stations(station_id) ON DELETE SET NULL ON UPDATE CASCADE,
	FOREIGN KEY (end_station_id) REFERENCES stations(station_id) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS "stations" (
	"station_id" bigint NOT NULL UNIQUE,
	"station_name" text NOT NULL,
	"station_longitude" varchar(255) NOT NULL,
	"station_latitude" varchar(255) NOT NULL,
	PRIMARY KEY ("station_id")
);
