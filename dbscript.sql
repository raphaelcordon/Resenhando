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

