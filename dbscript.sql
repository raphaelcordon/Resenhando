CREATE TABLE IF NOT EXISTS public."users" (
						ID serial PRIMARY KEY,
						USERNAME VARCHAR(50),
						NAME VARCHAR(50),
						SURNAME VARCHAR(50),
						PASSWORD VARCHAR(255)
						);

CREATE TABLE IF NOT EXISTS public."resenha" (
						ID serial PRIMARY KEY,
                        TIPO_REVIEW VARCHAR(30),
						AUTHOR_ID SMALLINT,
                        SPOTIFY_LINK VARCHAR(255),
						NOME_REVIEW VARCHAR(50),
						REVIEW TEXT,
						DATE_REGISTER DATE,
						IMGE_FILE VARCHAR(255)
						);


CREATE TABLE IF NOT EXISTS public."comentarios" (
						ID serial PRIMARY KEY,
						RESENHA_ID SMALLINT,
						USER_ID SMALLINT,
						REVIEW TEXT,
						DATE DATE
						);

CREATE TABLE IF NOT EXISTS public."login_hist" (
						ID serial PRIMARY KEY,
						USER_ID SMALLINT,
						LOGIN_DATE TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
						);

CREATE TABLE IF NOT EXISTS public."curtidas_hist" (
						ID serial PRIMARY KEY,
						USER_ID SMALLINT,
						RESENHA_ID SMALLINT,
						LOGIN_DATE TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
						);