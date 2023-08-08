--
-- PostgreSQL database cluster dump
--

SET default_transaction_read_only = off;

SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;

--
-- Drop databases (except postgres and template1)
--

DROP DATABASE db_name;




--
-- Drop roles
--

DROP ROLE db_user;


--
-- Roles
--

CREATE ROLE db_user;
ALTER ROLE db_user WITH SUPERUSER INHERIT CREATEROLE CREATEDB LOGIN REPLICATION BYPASSRLS PASSWORD 'md5c6eff08c433a190ac15326e048403089';






--
-- Databases
--

--
-- Database "template1" dump
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 13.0
-- Dumped by pg_dump version 13.0

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

UPDATE pg_catalog.pg_database SET datistemplate = false WHERE datname = 'template1';
DROP DATABASE template1;
--
-- Name: template1; Type: DATABASE; Schema: -; Owner: db_user
--

CREATE DATABASE template1 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.utf8';


ALTER DATABASE template1 OWNER TO db_user;

\connect template1

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

--
-- Name: DATABASE template1; Type: COMMENT; Schema: -; Owner: db_user
--

COMMENT ON DATABASE template1 IS 'default template for new databases';


--
-- Name: template1; Type: DATABASE PROPERTIES; Schema: -; Owner: db_user
--

ALTER DATABASE template1 IS_TEMPLATE = true;


\connect template1

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

--
-- Name: DATABASE template1; Type: ACL; Schema: -; Owner: db_user
--

REVOKE CONNECT,TEMPORARY ON DATABASE template1 FROM PUBLIC;
GRANT CONNECT ON DATABASE template1 TO PUBLIC;


--
-- PostgreSQL database dump complete
--

--
-- Database "db_name" dump
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 13.0
-- Dumped by pg_dump version 13.0

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

--
-- Name: db_name; Type: DATABASE; Schema: -; Owner: db_user
--

CREATE DATABASE db_name WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.utf8';


ALTER DATABASE db_name OWNER TO db_user;

\connect db_name

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

--
-- Name: notification; Type: SCHEMA; Schema: -; Owner: db_user
--

CREATE SCHEMA notification;


ALTER SCHEMA notification OWNER TO db_user;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: configs; Type: TABLE; Schema: notification; Owner: db_user
--

CREATE TABLE notification.configs (
    id uuid NOT NULL,
    name character varying(255) NOT NULL,
    description text,
    value character varying(255) NOT NULL
);


ALTER TABLE notification.configs OWNER TO db_user;

--
-- Name: schedules; Type: TABLE; Schema: notification; Owner: db_user
--

CREATE TABLE notification.schedules (
    created timestamp with time zone NOT NULL,
    modified timestamp with time zone NOT NULL,
    id uuid NOT NULL,
    name character varying(255) NOT NULL,
    description text,
    template_params text,
    "group" character varying(100) NOT NULL,
    timing character varying(100) NOT NULL,
    priority character varying(100) NOT NULL,
    last_date timestamp with time zone,
    planned_date timestamp with time zone,
    urgent boolean NOT NULL,
    template_id uuid NOT NULL
);


ALTER TABLE notification.schedules OWNER TO db_user;

--
-- Name: templates; Type: TABLE; Schema: notification; Owner: db_user
--

CREATE TABLE notification.templates (
    created timestamp with time zone NOT NULL,
    modified timestamp with time zone NOT NULL,
    id uuid NOT NULL,
    name character varying(255) NOT NULL,
    description text,
    transport_type character varying(100) NOT NULL,
    task character varying(100) NOT NULL,
    theme text,
    template_body text NOT NULL
);


ALTER TABLE notification.templates OWNER TO db_user;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: db_user
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO db_user;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: db_user
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO db_user;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: db_user
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: db_user
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO db_user;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: db_user
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO db_user;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: db_user
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: db_user
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO db_user;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: db_user
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO db_user;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: db_user
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: db_user
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO db_user;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: db_user
--

CREATE TABLE public.auth_user_groups (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO db_user;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: db_user
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO db_user;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: db_user
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: db_user
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO db_user;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: db_user
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: db_user
--

CREATE TABLE public.auth_user_user_permissions (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO db_user;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: db_user
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO db_user;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: db_user
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: db_user
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO db_user;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: db_user
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO db_user;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: db_user
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: db_user
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO db_user;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: db_user
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO db_user;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: db_user
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: db_user
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO db_user;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: db_user
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO db_user;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: db_user
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: db_user
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO db_user;

--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Data for Name: configs; Type: TABLE DATA; Schema: notification; Owner: db_user
--

COPY notification.configs (id, name, description, value) FROM stdin;
\.


--
-- Data for Name: schedules; Type: TABLE DATA; Schema: notification; Owner: db_user
--

COPY notification.schedules (created, modified, id, name, description, template_params, "group", timing, priority, last_date, planned_date, urgent, template_id) FROM stdin;
\.


--
-- Data for Name: templates; Type: TABLE DATA; Schema: notification; Owner: db_user
--

COPY notification.templates (created, modified, id, name, description, transport_type, task, theme, template_body) FROM stdin;
2023-08-08 17:50:28.947057+00	2023-08-08 17:50:28.947067+00	d901cd22-4cc1-4d62-a6ab-0c2f39478798	Welcome	Welcome	email	set_rating	Welcome	<!doctype html>\r\n<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml"\r\n      xmlns:o="urn:schemas-microsoft-com:office:office">\r\n<head>\r\n  <!-- NAME: 1 COLUMN -->\r\n  <!--[if gte mso 15]>\r\n  <xml>\r\n    <o:OfficeDocumentSettings>\r\n      <o:AllowPNG/>\r\n      <o:PixelsPerInch>96</o:PixelsPerInch>\r\n    </o:OfficeDocumentSettings>\r\n  </xml>\r\n  <![endif]-->\r\n  <meta charset="UTF-8">\r\n  <meta http-equiv="X-UA-Compatible" content="IE=edge">\r\n  <meta name="viewport" content="width=device-width, initial-scale=1">\r\n  <title>*|MC:SUBJECT|*</title>\r\n\r\n  <style type="text/css">\r\n    p {\r\n      margin: 10px 0;\r\n      padding: 0;\r\n    }\r\n\r\n    table {\r\n      border-collapse: collapse;\r\n    }\r\n\r\n    h1, h2, h3, h4, h5, h6 {\r\n      display: block;\r\n      margin: 0;\r\n      padding: 0;\r\n    }\r\n\r\n    img, a img {\r\n      border: 0;\r\n      height: auto;\r\n      outline: none;\r\n      text-decoration: none;\r\n    }\r\n\r\n    body, #bodyTable, #bodyCell {\r\n      height: 100%;\r\n      margin: 0;\r\n      padding: 0;\r\n      width: 100%;\r\n    }\r\n\r\n    .mcnPreviewText {\r\n      display: none !important;\r\n    }\r\n\r\n    #outlook a {\r\n      padding: 0;\r\n    }\r\n\r\n    img {\r\n      -ms-interpolation-mode: bicubic;\r\n    }\r\n\r\n    table {\r\n      mso-table-lspace: 0pt;\r\n      mso-table-rspace: 0pt;\r\n    }\r\n\r\n    .ReadMsgBody {\r\n      width: 100%;\r\n    }\r\n\r\n    .ExternalClass {\r\n      width: 100%;\r\n    }\r\n\r\n    p, a, li, td, blockquote {\r\n      mso-line-height-rule: exactly;\r\n    }\r\n\r\n    a[href^=tel], a[href^=sms] {\r\n      color: inherit;\r\n      cursor: default;\r\n      text-decoration: none;\r\n    }\r\n\r\n    p, a, li, td, body, table, blockquote {\r\n      -ms-text-size-adjust: 100%;\r\n      -webkit-text-size-adjust: 100%;\r\n    }\r\n\r\n    .ExternalClass, .ExternalClass p, .ExternalClass td, .ExternalClass div, .ExternalClass span, .ExternalClass font {\r\n      line-height: 100%;\r\n    }\r\n\r\n    a[x-apple-data-detectors] {\r\n      color: inherit !important;\r\n      text-decoration: none !important;\r\n      font-size: inherit !important;\r\n      font-family: inherit !important;\r\n      font-weight: inherit !important;\r\n      line-height: inherit !important;\r\n    }\r\n\r\n    #bodyCell {\r\n      padding: 10px;\r\n    }\r\n\r\n    .templateContainer {\r\n      max-width: 600px !important;\r\n    }\r\n\r\n    a.mcnButton {\r\n      display: block;\r\n    }\r\n\r\n    .mcnImage, .mcnRetinaImage {\r\n      vertical-align: bottom;\r\n    }\r\n\r\n    .mcnTextContent {\r\n      word-break: break-word;\r\n    }\r\n\r\n    .mcnTextContent img {\r\n      height: auto !important;\r\n    }\r\n\r\n    .mcnDividerBlock {\r\n      table-layout: fixed !important;\r\n    }\r\n\r\n    /*\r\n      @tab Page\r\n      @section Background Style\r\n      @tip Set the background color and top border for your email. You may want to choose colors that match your company's branding.\r\n      */\r\n    body, #bodyTable {\r\n      /*@editable*/\r\n      background-color: #FAFAFA;\r\n    }\r\n\r\n    /*\r\n      @tab Page\r\n      @section Background Style\r\n      @tip Set the background color and top border for your email. You may want to choose colors that match your company's branding.\r\n      */\r\n    #bodyCell {\r\n      /*@editable*/\r\n      border-top: 0;\r\n    }\r\n\r\n    /*\r\n      @tab Page\r\n      @section Email Border\r\n      @tip Set the border for your email.\r\n      */\r\n    .templateContainer {\r\n      /*@editable*/\r\n      border: 0;\r\n    }\r\n\r\n    /*\r\n      @tab Page\r\n      @section Heading 1\r\n      @tip Set the styling for all first-level headings in your emails. These should be the largest of your headings.\r\n      @style heading 1\r\n      */\r\n    h1 {\r\n      /*@editable*/\r\n      color: #202020;\r\n      /*@editable*/\r\n      font-family: Helvetica;\r\n      /*@editable*/\r\n      font-size: 26px;\r\n      /*@editable*/\r\n      font-style: normal;\r\n      /*@editable*/\r\n      font-weight: bold;\r\n      /*@editable*/\r\n      line-height: 125%;\r\n      /*@editable*/\r\n      letter-spacing: normal;\r\n      /*@editable*/\r\n      text-align: left;\r\n    }\r\n\r\n    /*\r\n      @tab Page\r\n      @section Heading 2\r\n      @tip Set the styling for all second-level headings in your emails.\r\n      @style heading 2\r\n      */\r\n    h2 {\r\n      /*@editable*/\r\n      color: #202020;\r\n      /*@editable*/\r\n      font-family: Helvetica;\r\n      /*@editable*/\r\n      font-size: 22px;\r\n      /*@editable*/\r\n      font-style: normal;\r\n      /*@editable*/\r\n      font-weight: bold;\r\n      /*@editable*/\r\n      line-height: 125%;\r\n      /*@editable*/\r\n      letter-spacing: normal;\r\n      /*@editable*/\r\n      text-align: left;\r\n    }\r\n\r\n    /*\r\n      @tab Page\r\n      @section Heading 3\r\n      @tip Set the styling for all third-level headings in your emails.\r\n      @style heading 3\r\n      */\r\n    h3 {\r\n      /*@editable*/\r\n      color: #202020;\r\n      /*@editable*/\r\n      font-family: Helvetica;\r\n      /*@editable*/\r\n      font-size: 20px;\r\n      /*@editable*/\r\n      font-style: normal;\r\n      /*@editable*/\r\n      font-weight: bold;\r\n      /*@editable*/\r\n      line-height: 125%;\r\n      /*@editable*/\r\n      letter-spacing: normal;\r\n      /*@editable*/\r\n      text-align: left;\r\n    }\r\n\r\n    /*\r\n      @tab Page\r\n      @section Heading 4\r\n      @tip Set the styling for all fourth-level headings in your emails. These should be the smallest of your headings.\r\n      @style heading 4\r\n      */\r\n    h4 {\r\n      /*@editable*/\r\n      color: #202020;\r\n      /*@editable*/\r\n      font-family: Helvetica;\r\n      /*@editable*/\r\n      font-size: 18px;\r\n      /*@editable*/\r\n      font-style: normal;\r\n      /*@editable*/\r\n      font-weight: bold;\r\n      /*@editable*/\r\n      line-height: 125%;\r\n      /*@editable*/\r\n      letter-spacing: normal;\r\n      /*@editable*/\r\n      text-align: left;\r\n    }\r\n\r\n    /*\r\n      @tab Preheader\r\n      @section Preheader Style\r\n      @tip Set the background color and borders for your email's preheader area.\r\n      */\r\n    #templatePreheader {\r\n      /*@editable*/\r\n      background-color: #FAFAFA;\r\n      /*@editable*/\r\n      background-image: none;\r\n      /*@editable*/\r\n      background-repeat: no-repeat;\r\n      /*@editable*/\r\n      background-position: center;\r\n      /*@editable*/\r\n      background-size: cover;\r\n      /*@editable*/\r\n      border-top: 0;\r\n      /*@editable*/\r\n      border-bottom: 0;\r\n      /*@editable*/\r\n      padding-top: 9px;\r\n      /*@editable*/\r\n      padding-bottom: 9px;\r\n    }\r\n\r\n    /*\r\n      @tab Preheader\r\n      @section Preheader Text\r\n      @tip Set the styling for your email's preheader text. Choose a size and color that is easy to read.\r\n      */\r\n    #templatePreheader .mcnTextContent, #templatePreheader .mcnTextContent p {\r\n      /*@editable*/\r\n      color: #656565;\r\n      /*@editable*/\r\n      font-family: Helvetica;\r\n      /*@editable*/\r\n      font-size: 12px;\r\n      /*@editable*/\r\n      line-height: 150%;\r\n      /*@editable*/\r\n      text-align: left;\r\n    }\r\n\r\n    /*\r\n      @tab Preheader\r\n      @section Preheader Link\r\n      @tip Set the styling for your email's preheader links. Choose a color that helps them stand out from your text.\r\n      */\r\n    #templatePreheader .mcnTextContent a, #templatePreheader .mcnTextContent p a {\r\n      /*@editable*/\r\n      color: #656565;\r\n      /*@editable*/\r\n      font-weight: normal;\r\n      /*@editable*/\r\n      text-decoration: underline;\r\n    }\r\n\r\n    /*\r\n      @tab Header\r\n      @section Header Style\r\n      @tip Set the background color and borders for your email's header area.\r\n      */\r\n    #templateHeader {\r\n      /*@editable*/\r\n      background-color: #FFFFFF;\r\n      /*@editable*/\r\n      background-image: none;\r\n      /*@editable*/\r\n      background-repeat: no-repeat;\r\n      /*@editable*/\r\n      background-position: center;\r\n      /*@editable*/\r\n      background-size: cover;\r\n      /*@editable*/\r\n      border-top: 0;\r\n      /*@editable*/\r\n      border-bottom: 0;\r\n      /*@editable*/\r\n      padding-top: 9px;\r\n      /*@editable*/\r\n      padding-bottom: 0;\r\n    }\r\n\r\n    /*\r\n      @tab Header\r\n      @section Header Text\r\n      @tip Set the styling for your email's header text. Choose a size and color that is easy to read.\r\n      */\r\n    #templateHeader .mcnTextContent, #templateHeader .mcnTextContent p {\r\n      /*@editable*/\r\n      color: #202020;\r\n      /*@editable*/\r\n      font-family: Helvetica;\r\n      /*@editable*/\r\n      font-size: 16px;\r\n      /*@editable*/\r\n      line-height: 150%;\r\n      /*@editable*/\r\n      text-align: left;\r\n    }\r\n\r\n    /*\r\n      @tab Header\r\n      @section Header Link\r\n      @tip Set the styling for your email's header links. Choose a color that helps them stand out from your text.\r\n      */\r\n    #templateHeader .mcnTextContent a, #templateHeader .mcnTextContent p a {\r\n      /*@editable*/\r\n      color: #007C89;\r\n      /*@editable*/\r\n      font-weight: normal;\r\n      /*@editable*/\r\n      text-decoration: underline;\r\n    }\r\n\r\n    /*\r\n      @tab Body\r\n      @section Body Style\r\n      @tip Set the background color and borders for your email's body area.\r\n      */\r\n    #templateBody {\r\n      /*@editable*/\r\n      background-color: #FFFFFF;\r\n      /*@editable*/\r\n      background-image: none;\r\n      /*@editable*/\r\n      background-repeat: no-repeat;\r\n      /*@editable*/\r\n      background-position: center;\r\n      /*@editable*/\r\n      background-size: cover;\r\n      /*@editable*/\r\n      border-top: 0;\r\n      /*@editable*/\r\n      border-bottom: 2px solid #EAEAEA;\r\n      /*@editable*/\r\n      padding-top: 0;\r\n      /*@editable*/\r\n      padding-bottom: 9px;\r\n    }\r\n\r\n    /*\r\n      @tab Body\r\n      @section Body Text\r\n      @tip Set the styling for your email's body text. Choose a size and color that is easy to read.\r\n      */\r\n    #templateBody .mcnTextContent, #templateBody .mcnTextContent p {\r\n      /*@editable*/\r\n      color: #202020;\r\n      /*@editable*/\r\n      font-family: Helvetica;\r\n      /*@editable*/\r\n      font-size: 16px;\r\n      /*@editable*/\r\n      line-height: 150%;\r\n      /*@editable*/\r\n      text-align: left;\r\n    }\r\n\r\n    /*\r\n      @tab Body\r\n      @section Body Link\r\n      @tip Set the styling for your email's body links. Choose a color that helps them stand out from your text.\r\n      */\r\n    #templateBody .mcnTextContent a, #templateBody .mcnTextContent p a {\r\n      /*@editable*/\r\n      color: #007C89;\r\n      /*@editable*/\r\n      font-weight: normal;\r\n      /*@editable*/\r\n      text-decoration: underline;\r\n    }\r\n\r\n    /*\r\n      @tab Footer\r\n      @section Footer Style\r\n      @tip Set the background color and borders for your email's footer area.\r\n      */\r\n    #templateFooter {\r\n      /*@editable*/\r\n      background-color: #FAFAFA;\r\n      /*@editable*/\r\n      background-image: none;\r\n      /*@editable*/\r\n      background-repeat: no-repeat;\r\n      /*@editable*/\r\n      background-position: center;\r\n      /*@editable*/\r\n      background-size: cover;\r\n      /*@editable*/\r\n      border-top: 0;\r\n      /*@editable*/\r\n      border-bottom: 0;\r\n      /*@editable*/\r\n      padding-top: 9px;\r\n      /*@editable*/\r\n      padding-bottom: 9px;\r\n    }\r\n\r\n    /*\r\n      @tab Footer\r\n      @section Footer Text\r\n      @tip Set the styling for your email's footer text. Choose a size and color that is easy to read.\r\n      */\r\n    #templateFooter .mcnTextContent, #templateFooter .mcnTextContent p {\r\n      /*@editable*/\r\n      color: #656565;\r\n      /*@editable*/\r\n      font-family: Helvetica;\r\n      /*@editable*/\r\n      font-size: 12px;\r\n      /*@editable*/\r\n      line-height: 150%;\r\n      /*@editable*/\r\n      text-align: center;\r\n    }\r\n\r\n    /*\r\n      @tab Footer\r\n      @section Footer Link\r\n      @tip Set the styling for your email's footer links. Choose a color that helps them stand out from your text.\r\n      */\r\n    #templateFooter .mcnTextContent a, #templateFooter .mcnTextContent p a {\r\n      /*@editable*/\r\n      color: #656565;\r\n      /*@editable*/\r\n      font-weight: normal;\r\n      /*@editable*/\r\n      text-decoration: underline;\r\n    }\r\n\r\n    @media only screen and (min-width: 768px) {\r\n      .templateContainer {\r\n        width: 600px !important;\r\n      }\r\n\r\n    }\r\n\r\n    @media only screen and (max-width: 480px) {\r\n      body, table, td, p, a, li, blockquote {\r\n        -webkit-text-size-adjust: none !important;\r\n      }\r\n\r\n    }\r\n\r\n    @media only screen and (max-width: 480px) {\r\n      body {\r\n        width: 100% !important;\r\n        min-width: 100% !important;\r\n      }\r\n\r\n    }\r\n\r\n    @media only screen and (max-width: 480px) {\r\n      .mcnRetinaImage {\r\n        max-width: 100% !important;\r\n      }\r\n\r\n    }\r\n\r\n    @media only screen and (max-width: 480px) {\r\n      .mcnImage {\r\n        width: 100% !important;\r\n      }\r\n\r\n    }\r\n\r\n    @media only screen and (max-width: 480px) {\r\n      .mcnCartContainer, .mcnCaptionTopContent, .mcnRecContentContainer, .mcnCaptionBottomContent, .mcnTextContentContainer, .mcnBoxedTextContentContainer, .mcnImageGroupContentContainer, .mcnCaptionLeftTextContentContainer, .mcnCaptionRightTextContentContainer, .mcnCaptionLeftImageContentContainer, .mcnCaptionRightImageContentContainer, .mcnImageCardLeftTextContentContainer, .mcnImageCardRightTextContentContainer, .mcnImageCardLeftImageContentContainer, .mcnImageCardRightImageContentContainer {\r\n        max-width: 100% !important;\r\n        width: 100% !important;\r\n      }\r\n\r\n    }\r\n\r\n    @media only screen and (max-width: 480px) {\r\n      .mcnBoxedTextContentContainer {\r\n        min-width: 100% !important;\r\n      }\r\n\r\n    }\r\n\r\n    @media only screen and (max-width: 480px) {\r\n      .mcnImageGroupContent {\r\n        padding: 9px !important;\r\n      }\r\n\r\n    }\r\n\r\n    @media only screen and (max-width: 480px) {\r\n      .mcnCaptionLeftContentOuter .mcnTextContent, .mcnCaptionRightContentOuter .mcnTextContent {\r\n        padding-top: 9px !important;\r\n      }\r\n\r\n    }\r\n\r\n    @media only screen and (max-width: 480px) {\r\n      .mcnImageCardTopImageContent, .mcnCaptionBottomContent:last-child .mcnCaptionBottomImageContent, .mcnCaptionBlockInner .mcnCaptionTopContent:last-child .mcnTextContent {\r\n        padding-top: 18px !important;\r\n      }\r\n\r\n    }\r\n\r\n    @media only screen and (max-width: 480px) {\r\n      .mcnImageCardBottomImageContent {\r\n        padding-bottom: 9px !important;\r\n      }\r\n\r\n    }\r\n\r\n    @media only screen and (max-width: 480px) {\r\n      .mcnImageGroupBlockInner {\r\n        padding-top: 0 !important;\r\n        padding-bottom: 0 !important;\r\n      }\r\n\r\n    }\r\n\r\n    @media only screen and (max-width: 480px) {\r\n      .mcnImageGroupBlockOuter {\r\n        padding-top: 9px !important;\r\n        padding-bottom: 9px !important;\r\n      }\r\n\r\n    }\r\n\r\n    @media only screen and (max-width: 480px) {\r\n      .mcnTextContent, .mcnBoxedTextContentColumn {\r\n        padding-right: 18px !important;\r\n        padding-left: 18px !important;\r\n      }\r\n\r\n    }\r\n\r\n    @media only screen and (max-width: 480px) {\r\n      .mcnImageCardLeftImageContent, .mcnImageCardRightImageContent {\r\n        padding-right: 18px !important;\r\n        padding-bottom: 0 !important;\r\n        padding-left: 18px !important;\r\n      }\r\n\r\n    }\r\n\r\n    @media only screen and (max-width: 480px) {\r\n      .mcpreview-image-uploader {\r\n        display: none !important;\r\n        width: 100% !important;\r\n      }\r\n\r\n    }\r\n\r\n    @media only screen and (max-width: 480px) {\r\n      /*\r\n        @tab Mobile Styles\r\n        @section Heading 1\r\n        @tip Make the first-level headings larger in size for better readability on small screens.\r\n        */\r\n      h1 {\r\n        /*@editable*/\r\n        font-size: 22px !important;\r\n        /*@editable*/\r\n        line-height: 125% !important;\r\n      }\r\n\r\n    }\r\n\r\n    @media only screen and (max-width: 480px) {\r\n      /*\r\n        @tab Mobile Styles\r\n        @section Heading 2\r\n        @tip Make the second-level headings larger in size for better readability on small screens.\r\n        */\r\n      h2 {\r\n        /*@editable*/\r\n        font-size: 20px !important;\r\n        /*@editable*/\r\n        line-height: 125% !important;\r\n      }\r\n\r\n    }\r\n\r\n    @media only screen and (max-width: 480px) {\r\n      /*\r\n        @tab Mobile Styles\r\n        @section Heading 3\r\n        @tip Make the third-level headings larger in size for better readability on small screens.\r\n        */\r\n      h3 {\r\n        /*@editable*/\r\n        font-size: 18px !important;\r\n        /*@editable*/\r\n        line-height: 125% !important;\r\n      }\r\n\r\n    }\r\n\r\n    @media only screen and (max-width: 480px) {\r\n      /*\r\n        @tab Mobile Styles\r\n        @section Heading 4\r\n        @tip Make the fourth-level headings larger in size for better readability on small screens.\r\n        */\r\n      h4 {\r\n        /*@editable*/\r\n        font-size: 16px !important;\r\n        /*@editable*/\r\n        line-height: 150% !important;\r\n      }\r\n\r\n    }\r\n\r\n    @media only screen and (max-width: 480px) {\r\n      /*\r\n        @tab Mobile Styles\r\n        @section Boxed Text\r\n        @tip Make the boxed text larger in size for better readability on small screens. We recommend a font size of at least 16px.\r\n        */\r\n      .mcnBoxedTextContentContainer .mcnTextContent, .mcnBoxedTextContentContainer .mcnTextContent p {\r\n        /*@editable*/\r\n        font-size: 14px !important;\r\n        /*@editable*/\r\n        line-height: 150% !important;\r\n      }\r\n\r\n    }\r\n\r\n    @media only screen and (max-width: 480px) {\r\n      /*\r\n        @tab Mobile Styles\r\n        @section Preheader Visibility\r\n        @tip Set the visibility of the email's preheader on small screens. You can hide it to save space.\r\n        */\r\n      #templatePreheader {\r\n        /*@editable*/\r\n        display: block !important;\r\n      }\r\n\r\n    }\r\n\r\n    @media only screen and (max-width: 480px) {\r\n      /*\r\n        @tab Mobile Styles\r\n        @section Preheader Text\r\n        @tip Make the preheader text larger in size for better readability on small screens.\r\n        */\r\n      #templatePreheader .mcnTextContent, #templatePreheader .mcnTextContent p {\r\n        /*@editable*/\r\n        font-size: 14px !important;\r\n        /*@editable*/\r\n        line-height: 150% !important;\r\n      }\r\n\r\n    }\r\n\r\n    @media only screen and (max-width: 480px) {\r\n      /*\r\n        @tab Mobile Styles\r\n        @section Header Text\r\n        @tip Make the header text larger in size for better readability on small screens.\r\n        */\r\n      #templateHeader .mcnTextContent, #templateHeader .mcnTextContent p {\r\n        /*@editable*/\r\n        font-size: 16px !important;\r\n        /*@editable*/\r\n        line-height: 150% !important;\r\n      }\r\n\r\n    }\r\n\r\n    @media only screen and (max-width: 480px) {\r\n      /*\r\n        @tab Mobile Styles\r\n        @section Body Text\r\n        @tip Make the body text larger in size for better readability on small screens. We recommend a font size of at least 16px.\r\n        */\r\n      #templateBody .mcnTextContent, #templateBody .mcnTextContent p {\r\n        /*@editable*/\r\n        font-size: 16px !important;\r\n        /*@editable*/\r\n        line-height: 150% !important;\r\n      }\r\n\r\n    }\r\n\r\n    @media only screen and (max-width: 480px) {\r\n      /*\r\n        @tab Mobile Styles\r\n        @section Footer Text\r\n        @tip Make the footer content text larger in size for better readability on small screens.\r\n        */\r\n      #templateFooter .mcnTextContent, #templateFooter .mcnTextContent p {\r\n        /*@editable*/\r\n        font-size: 14px !important;\r\n        /*@editable*/\r\n        line-height: 150% !important;\r\n      }\r\n\r\n    }</style>\r\n</head>\r\n<body>\r\n<!--*|IF:MC_PREVIEW_TEXT|*-->\r\n<!--[if !gte mso 9]><!----><span class="mcnPreviewText"\r\n                                 style="display:none; font-size:0px; line-height:0px; max-height:0px; max-width:0px; opacity:0; overflow:hidden; visibility:hidden; mso-hide:all;"></span>\r\n<!--<![endif]-->\r\n<!--*|END:IF|*-->\r\n<center>\r\n  <table align="center" border="0" cellpadding="0" cellspacing="0" height="100%" width="100%" id="bodyTable">\r\n    <tr>\r\n      <td align="center" valign="top" id="bodyCell">\r\n        <!-- BEGIN TEMPLATE // -->\r\n        <!--[if (gte mso 9)|(IE)]>\r\n        <table align="center" border="0" cellspacing="0" cellpadding="0" width="600" style="width:600px;">\r\n          <tr>\r\n            <td align="center" valign="top" width="600" style="width:600px;">\r\n        <![endif]-->\r\n        <table border="0" cellpadding="0" cellspacing="0" width="100%" class="templateContainer">\r\n          <tr>\r\n            <td valign="top" id="templatePreheader">\r\n              <table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnImageBlock"\r\n                     style="min-width:100%;">\r\n                <tbody class="mcnImageBlockOuter">\r\n                <tr>\r\n                  <td valign="top" style="padding:9px" class="mcnImageBlockInner">\r\n                    <table align="left" width="100%" border="0" cellpadding="0" cellspacing="0"\r\n                           class="mcnImageContentContainer" style="min-width:100%;">\r\n                      <tbody>\r\n                      <tr>\r\n                        <td class="mcnImageContent" valign="top"\r\n                            style="padding-right: 9px; padding-left: 9px; padding-top: 0; padding-bottom: 0; text-align:center;">\r\n\r\n\r\n                          <img align="center" alt=""\r\n                               src="https://mcusercontent.com/597bc5462e8302e1e9db1d857/images/7307dfb2-ccc5-4923-937b-4f833c61c341.png"\r\n                               width="221"\r\n                               style="max-width:221px; padding-bottom: 0; display: inline !important; vertical-align: bottom;"\r\n                               class="mcnImage">\r\n\r\n\r\n                        </td>\r\n                      </tr>\r\n                      </tbody>\r\n                    </table>\r\n                  </td>\r\n                </tr>\r\n                </tbody>\r\n              </table>\r\n            </td>\r\n          </tr>\r\n          <tr>\r\n            <td valign="top" id="templateHeader">\r\n              <table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock"\r\n                     style="min-width:100%;">\r\n                <tbody class="mcnTextBlockOuter">\r\n                <tr>\r\n                  <td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">\r\n                    <!--[if mso]>\r\n                    <table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">\r\n                      <tr>\r\n                    <![endif]-->\r\n\r\n                    <!--[if mso]>\r\n                    <td valign="top" width="600" style="width:600px;">\r\n                    <![endif]-->\r\n                    <table align="left" border="0" cellpadding="0" cellspacing="0"\r\n                           style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">\r\n                      <tbody>\r\n                      <tr>\r\n\r\n                        <td valign="top" class="mcnTextContent"\r\n                            style="padding-top:0; padding-right:18px; padding-bottom:9px; padding-left:18px;">\r\n\r\n                          <h1 class="mc-toc-title" style="text-align: center;">{{ title }}</h1>\r\n\r\n                        </td>\r\n                      </tr>\r\n                      </tbody>\r\n                    </table>\r\n                    <!--[if mso]>\r\n                    </td>\r\n                    <![endif]-->\r\n\r\n                    <!--[if mso]>\r\n                    </tr>\r\n                    </table>\r\n                    <![endif]-->\r\n                  </td>\r\n                </tr>\r\n                </tbody>\r\n              </table>\r\n              <table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnImageBlock"\r\n                     style="min-width:100%;">\r\n                <tbody class="mcnImageBlockOuter">\r\n                <tr>\r\n                  <td valign="top" style="padding:9px" class="mcnImageBlockInner">\r\n                    <table align="left" width="100%" border="0" cellpadding="0" cellspacing="0"\r\n                           class="mcnImageContentContainer" style="min-width:100%;">\r\n                      <tbody>\r\n                      <tr>\r\n                        <td class="mcnImageContent" valign="top"\r\n                            style="padding-right: 9px; padding-left: 9px; padding-top: 0; padding-bottom: 0; text-align:center;">\r\n\r\n                          <img align="center" alt=""\r\n                               src="{{ image }}"\r\n                               width="564"\r\n                               style="max-width:1000px; padding-bottom: 0; display: inline !important; vertical-align: bottom;"\r\n                               class="mcnImage">\r\n                        </td>\r\n                      </tr>\r\n                      </tbody>\r\n                    </table>\r\n                  </td>\r\n                </tr>\r\n                </tbody>\r\n              </table>\r\n            </td>\r\n          </tr>\r\n          <tr>\r\n            <td valign="top" id="templateBody">\r\n              <table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock"\r\n                     style="min-width:100%;">\r\n                <tbody class="mcnTextBlockOuter">\r\n                <tr>\r\n                  <td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">\r\n                    <!--[if mso]>\r\n                    <table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">\r\n                      <tr>\r\n                    <![endif]-->\r\n\r\n                    <!--[if mso]>\r\n                    <td valign="top" width="600" style="width:600px;">\r\n                    <![endif]-->\r\n                    <table align="left" border="0" cellpadding="0" cellspacing="0"\r\n                           style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">\r\n                      <tbody>\r\n                      <tr>\r\n\r\n                        <td valign="top" class="mcnTextContent"\r\n                            style="padding-top:0; padding-right:18px; padding-bottom:9px; padding-left:18px;">\r\n\r\n                          <h1 style="text-align: center;">{{ text }}</h1>\r\n\r\n                        </td>\r\n                      </tr>\r\n                      </tbody>\r\n                    </table>\r\n                    <!--[if mso]>\r\n                    </td>\r\n                    <![endif]-->\r\n\r\n                    <!--[if mso]>\r\n                    </tr>\r\n                    </table>\r\n                    <![endif]-->\r\n                  </td>\r\n                </tr>\r\n                </tbody>\r\n              </table>\r\n            </td>\r\n          </tr>\r\n          <tr>\r\n            <td valign="top" id="templateFooter"></td>\r\n          </tr>\r\n        </table>\r\n        <!--[if (gte mso 9)|(IE)]>\r\n        </td>\r\n        </tr>\r\n        </table>\r\n        <![endif]-->\r\n        <!-- // END TEMPLATE -->\r\n      </td>\r\n    </tr>\r\n  </table>\r\n</center>\r\n</body>\r\n</html>
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: db_user
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: db_user
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: db_user
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add config	7	add_configuration
26	Can change config	7	change_configuration
27	Can delete config	7	delete_configuration
28	Can view config	7	view_configuration
29	Can add template	8	add_template
30	Can change template	8	change_template
31	Can delete template	8	delete_template
32	Can view template	8	view_template
33	Can add schedule	9	add_schedule
34	Can change schedule	9	change_schedule
35	Can delete schedule	9	delete_schedule
36	Can view schedule	9	view_schedule
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: db_user
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$320000$gxY22LmZEro1uUWW3sQSaT$c1SMxC3dgZzopPbSUhExDL6OapBetf8CPMnjpborwmE=	2023-08-08 17:49:28.812927+00	t	ivan			ivan@ivan.ru	t	t	2023-08-08 17:47:08.329759+00
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: db_user
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: db_user
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: db_user
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2023-08-08 17:50:28.948954+00	d901cd22-4cc1-4d62-a6ab-0c2f39478798	Welcome	1	[{"added": {}}]	8	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: db_user
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	notification	configuration
8	notification	template
9	notification	schedule
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: db_user
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2023-08-08 17:46:46.906476+00
2	auth	0001_initial	2023-08-08 17:46:47.004399+00
3	admin	0001_initial	2023-08-08 17:46:47.030336+00
4	admin	0002_logentry_remove_auto_add	2023-08-08 17:46:47.037271+00
5	admin	0003_logentry_add_action_flag_choices	2023-08-08 17:46:47.04434+00
6	contenttypes	0002_remove_content_type_name	2023-08-08 17:46:47.058112+00
7	auth	0002_alter_permission_name_max_length	2023-08-08 17:46:47.06578+00
8	auth	0003_alter_user_email_max_length	2023-08-08 17:46:47.073727+00
9	auth	0004_alter_user_username_opts	2023-08-08 17:46:47.082123+00
10	auth	0005_alter_user_last_login_null	2023-08-08 17:46:47.08981+00
11	auth	0006_require_contenttypes_0002	2023-08-08 17:46:47.092408+00
12	auth	0007_alter_validators_add_error_messages	2023-08-08 17:46:47.099422+00
13	auth	0008_alter_user_username_max_length	2023-08-08 17:46:47.111214+00
14	auth	0009_alter_user_last_name_max_length	2023-08-08 17:46:47.119056+00
15	auth	0010_alter_group_name_max_length	2023-08-08 17:46:47.127286+00
16	auth	0011_update_proxy_permissions	2023-08-08 17:46:47.134484+00
17	auth	0012_alter_user_first_name_max_length	2023-08-08 17:46:47.142348+00
18	notification	0001_initial	2023-08-08 17:46:47.185877+00
19	sessions	0001_initial	2023-08-08 17:46:47.206683+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: db_user
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
v3rpfmec9ry2k93i684pj7xr1npmgxqg	.eJxVjMsOwiAQRf-FtSE8ChWX7v0GMjMMUjWQlHZl_HfbpAvdnnPufYsI61Li2nmOUxIXocXplyHQk-su0gPqvUlqdZknlHsiD9vlrSV-XY_276BAL9uatTXJeGctMQGOHMiZwCqMZzQK0Q06u40G8JxtcIpVZjRIQ1BZoRefL-ktODQ:1qTQpk:fcaoDuv6aU2jG9a9An5anQlauvZXYDrolrWdNZurNgk	2023-08-22 17:49:28.815841+00
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: db_user
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: db_user
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: db_user
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 36, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: db_user
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: db_user
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: db_user
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: db_user
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: db_user
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 9, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: db_user
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 19, true);


--
-- Name: configs configs_pkey; Type: CONSTRAINT; Schema: notification; Owner: db_user
--

ALTER TABLE ONLY notification.configs
    ADD CONSTRAINT configs_pkey PRIMARY KEY (id);


--
-- Name: schedules schedules_pkey; Type: CONSTRAINT; Schema: notification; Owner: db_user
--

ALTER TABLE ONLY notification.schedules
    ADD CONSTRAINT schedules_pkey PRIMARY KEY (id);


--
-- Name: templates templates_pkey; Type: CONSTRAINT; Schema: notification; Owner: db_user
--

ALTER TABLE ONLY notification.templates
    ADD CONSTRAINT templates_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: configs_name_66c7d274; Type: INDEX; Schema: notification; Owner: db_user
--

CREATE INDEX configs_name_66c7d274 ON notification.configs USING btree (name);


--
-- Name: configs_name_66c7d274_like; Type: INDEX; Schema: notification; Owner: db_user
--

CREATE INDEX configs_name_66c7d274_like ON notification.configs USING btree (name varchar_pattern_ops);


--
-- Name: schedules_template_id_b72e3ce4; Type: INDEX; Schema: notification; Owner: db_user
--

CREATE INDEX schedules_template_id_b72e3ce4 ON notification.schedules USING btree (template_id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: db_user
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: db_user
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: db_user
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: db_user
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: db_user
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: db_user
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: db_user
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: db_user
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: db_user
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: db_user
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: db_user
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: db_user
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: db_user
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: schedules schedules_template_id_b72e3ce4_fk_templates_id; Type: FK CONSTRAINT; Schema: notification; Owner: db_user
--

ALTER TABLE ONLY notification.schedules
    ADD CONSTRAINT schedules_template_id_b72e3ce4_fk_templates_id FOREIGN KEY (template_id) REFERENCES notification.templates(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: db_user
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

--
-- Database "postgres" dump
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 13.0
-- Dumped by pg_dump version 13.0

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

DROP DATABASE postgres;
--
-- Name: postgres; Type: DATABASE; Schema: -; Owner: db_user
--

CREATE DATABASE postgres WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.utf8';


ALTER DATABASE postgres OWNER TO db_user;

\connect postgres

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

--
-- Name: DATABASE postgres; Type: COMMENT; Schema: -; Owner: db_user
--

COMMENT ON DATABASE postgres IS 'default administrative connection database';


--
-- PostgreSQL database dump complete
--

--
-- PostgreSQL database cluster dump complete
--

