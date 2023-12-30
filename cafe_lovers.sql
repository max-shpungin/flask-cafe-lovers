--
-- PostgreSQL database dump
--

-- Dumped from database version 14.10 (Ubuntu 14.10-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.10 (Ubuntu 14.10-0ubuntu0.22.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

ALTER TABLE ONLY public.users_cafes DROP CONSTRAINT users_cafes_user_id_fkey;
ALTER TABLE ONLY public.users_cafes DROP CONSTRAINT users_cafes_cafe_id_fkey;
ALTER TABLE ONLY public.users DROP CONSTRAINT users_username_key;
ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
ALTER TABLE ONLY public.users_cafes DROP CONSTRAINT users_cafes_pkey;
ALTER TABLE ONLY public.cafes DROP CONSTRAINT cafes_pkey;
ALTER TABLE public.users ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.cafes ALTER COLUMN id DROP DEFAULT;
DROP SEQUENCE public.users_id_seq;
DROP TABLE public.users_cafes;
DROP TABLE public.users;
DROP SEQUENCE public.cafes_id_seq;
DROP TABLE public.cafes;
SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: cafes; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.cafes (
    id integer NOT NULL,
    name character varying(30) NOT NULL,
    address_street character varying(30) NOT NULL,
    address_state character varying(20) NOT NULL,
    image_url character varying(50)
);


--
-- Name: cafes_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.cafes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: cafes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.cafes_id_seq OWNED BY public.cafes.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username character varying(20) NOT NULL,
    password character varying(80) NOT NULL
);


--
-- Name: users_cafes; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.users_cafes (
    user_id integer NOT NULL,
    cafe_id integer NOT NULL
);


--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: cafes id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.cafes ALTER COLUMN id SET DEFAULT nextval('public.cafes_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: cafes; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.cafes (id, name, address_street, address_state, image_url) FROM stdin;
1	lemon cafe	123 grove street	california	default
2	dingdong coffee	45 jake blvd.	Nevada	default
3	Peet's Coffee	3401 Fruitvale Ave	California	default
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.users (id, username, password) FROM stdin;
1	jack	$2b$12$aIYF.OqtePdwueEFE3lfmuTzrS4L4/mPcTGOEffBR6s/dvy45I/j.
2	johnny	$2b$12$/imWK8Rp8mBoiFgHX/r00egaV3pM7KHc5UZhE8RbsD5ONw6nrORkm
3	test	$2b$12$qjQKIieOXeONwOPsWc38meEmXFlGmi/ijImZkl7Fp.qDJ32PVh/v.
4	fred	$2b$12$crHila4kVKRM9KEJ2Ii0tOTrD0YE9wiNcScDHmeEvMslTDYTBX7.i
\.


--
-- Data for Name: users_cafes; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.users_cafes (user_id, cafe_id) FROM stdin;
2	1
2	2
3	1
3	3
\.


--
-- Name: cafes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.cafes_id_seq', 3, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.users_id_seq', 4, true);


--
-- Name: cafes cafes_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.cafes
    ADD CONSTRAINT cafes_pkey PRIMARY KEY (id);


--
-- Name: users_cafes users_cafes_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users_cafes
    ADD CONSTRAINT users_cafes_pkey PRIMARY KEY (user_id, cafe_id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: users users_username_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);


--
-- Name: users_cafes users_cafes_cafe_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users_cafes
    ADD CONSTRAINT users_cafes_cafe_id_fkey FOREIGN KEY (cafe_id) REFERENCES public.cafes(id);


--
-- Name: users_cafes users_cafes_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users_cafes
    ADD CONSTRAINT users_cafes_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

