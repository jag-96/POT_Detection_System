drop table if exists sensors;

create table sensors(
	Time integer,
	Lat double,
	Lon double,
	GX double,
	GY double,
	GZ double,
	LidAngle double,
	LidDist double
);
