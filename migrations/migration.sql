CREATE TABLE store (
  "id" SERIAL NOT NULL,
  "name" VARCHAR(128) NOT NULL,
  "city" VARCHAR(128) NOT NULL,
  "state" VARCHAR(2) NOT NULL,
  "district" SMALLINT NOT NULL,
  "created_at" TIMESTAMP NOT NULL DEFAULT NOW(),
  "updated_at" TIMESTAMP NOT NULL DEFAULT NOW(),
  "deleted_at" TIMESTAMP,
  CONSTRAINT store_pkey PRIMARY KEY ("id")
);

CREATE TABLE transactions (
  "id" SERIAL NOT NULL,
  "store_id" SMALLINT REFERENCES store(id),
  "amount" INTEGER NOT NULL,
  "transaction_date" TIMESTAMP NOT NULL,
  "created_at" TIMESTAMP NOT NULL DEFAULT NOW(),
  "updated_at" TIMESTAMP NOT NULL DEFAULT NOW(),
  "deleted_at" TIMESTAMP,
  CONSTRAINT transaction_pkey PRIMARY KEY ("id")
);

CREATE TABLE user_data (
  "id" SERIAL NOT NULL,
  "first_name" VARCHAR(128) NOT NULL,
  "last_name" VARCHAR(128) NOT NULL,
  "email" VARCHAR(128) NOT NULL,
  "password" VARCHAR(128) NOT NULL,
  "user_type" SMALLINT NOT NULL,
  "created_at" TIMESTAMP NOT NULL DEFAULT NOW(),
  "updated_at" TIMESTAMP NOT NULL DEFAULT NOW(),
  "deleted_at" TIMESTAMP,
  CONSTRAINT user_data_pkey PRIMARY KEY ("id")
);

CREATE TABLE manager (
  "user_id" SMALLINT REFERENCES user_data(id),
  "store_id" SMALLINT REFERENCES store(id),
  "created_at" TIMESTAMP NOT NULL DEFAULT NOW(),
  "updated_at" TIMESTAMP NOT NULL DEFAULT NOW(),
  "deleted_at" TIMESTAMP,
  CONSTRAINT manager_pkey PRIMARY KEY ("user_id")
);

CREATE TABLE district_manager (
  "user_id" SMALLINT REFERENCES user_data(id),
  "district_id" SMALLINT NOT NULL,
  "created_at" TIMESTAMP NOT NULL DEFAULT NOW(),
  "updated_at" TIMESTAMP NOT NULL DEFAULT NOW(),
  "deleted_at" TIMESTAMP,
  CONSTRAINT district_manager_pkey PRIMARY KEY ("user_id")
);
