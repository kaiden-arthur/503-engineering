-- table construction 
DROP TABLE IF EXISTS patch CASCADE;
DROP TABLE IF EXISTS job CASCADE;
DROP TABLE IF EXISTS fight CASCADE;
DROP TABLE IF EXISTS job_actions CASCADE;
DROP TABLE IF EXISTS report CASCADE;
DROP TABLE IF EXISTS avg_potencies;

--- no dependencies first 
CREATE TABLE patch (  
	id SERIAL PRIMARY KEY,
	patch_number DECIMAL UNIQUE,
	start_time INTEGER, 
	end_time INTEGER
);

CREATE TABLE job ( 
	id SERIAL PRIMARY KEY,
	job_name VARCHAR UNIQUE, 
	job_role VARCHAR
);

CREATE TABLE avg_potencies(
	id SERIAL PRIMARY KEY, 
	avg_potency DECIMAL, 
	patch_number DECIMAL, 
	job_name VARCHAR, 
	FOREIGN KEY (job_name) REFERENCES job(job_name),
	FOREIGN KEY (patch_number) REFERENCES patch(patch_number) 
)

CREATE TABLE fight ( 
	fight_id SERIAL PRIMARY KEY,
	fight_name VARCHAR UNIQUE, 
	patch_number DECIMAL, 
	FOREIGN KEY (patch_number) REFERENCES patch(patch_number) 
);

CREATE TABLE job_actions( 
	id SERIAL PRIMARY KEY, 
	action_name VARCHAR, 
	potency INTEGER, 
	patch_number DECIMAL, 
	job_name VARCHAR, 
	FOREIGN KEY (patch_number) REFERENCES patch(patch_number), 
	FOREIGN KEY (job_name) REFERENCES job(job_name)
);
---then the join table 
CREATE TABLE report ( 
	id SERIAL PRIMARY KEY, 
	character_name VARCHAR, 
	dps DECIMAL, 
	damage_rank INTEGER, 
	patch_number NUMERIC, 
	job_name VARCHAR, 
	fight_name VARCHAR,
	FOREIGN KEY (patch_number) REFERENCES patch(patch_number), 
	FOREIGN KEY (job_name) REFERENCES job(job_name), 
	FOREIGN KEY (fight_name) REFERENCES fight(fight_name) 
);

COPY patch(patch_number, start_time, end_time) 
FROM 'C:\Users\Public\503 data\load_patch.csv'
WITH (FORMAT CSV, HEADER);

COPY job(job_name, job_role) 
FROM 'C:\Users\Public\503 data\load_jobs.csv'
WITH (FORMAT CSV, HEADER);

COPY avg_potencies(job_name, patch_number, avg_potency) 
FROM 'C:\Users\Public\503 data\load_avgs.csv'
WITH (FORMAT CSV, HEADER);

COPY fight(fight_name, patch_number) 
FROM 'C:\Users\Public\503 data\load_fights.csv'
WITH (FORMAT CSV, HEADER);

COPY job_actions (action_name, job_name, patch_number, potency) 
FROM 'C:\Users\Public\503 data\load_potencies.csv'
WITH (FORMAT CSV, HEADER);

COPY report(fight_name, character_name, job_name, dps, damage_rank, patch_number) 
FROM 'C:\Users\Public\503 data\load_reports.csv'
WITH (FORMAT CSV, HEADER);

SELECT * FROM report
LIMIT(5);