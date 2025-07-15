-- -----------------------------------------------------
-- File name: DB-Model.sql                             -
-- Date     : 2025-07-12                               -
-- Author   : Fábio Marques (fmarques@fmarques.eti.br) -
-- Purpose  : DDL structures for the ERP system        -
-- -----------------------------------------------------

-- -----------------------------------------------------
-- User entity
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS USER (
  ID           INT                NOT NULL PRIMARY KEY AUTO_INCREMENT,
  USERNAME     VARCHAR(45) UNIQUE NOT NULL,
  PASSWORD     VARCHAR(45)        NOT NULL,
  ACCESS_LEVEL INT                NOT NULL
);

INSERT INTO USER (USERNAME, PASSWORD, ACCESS_LEVEL) 
VALUES ('admin', MD5('admin'), 2);

-- -----------------------------------------------------
-- Product entity
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS PRODUCT (
  ID          INT            NOT NULL PRIMARY KEY AUTO_INCREMENT,
  NAME        VARCHAR(45)    NOT NULL,
  INGREDIENTS VARCHAR(1000),
  CATEGORY    VARCHAR(45)    NOT NULL,
  PRICE       FLOAT          NOT NULL
);

INSERT INTO PRODUCT (NAME, INGREDIENTS, CATEGORY, PRICE)
VALUES ('PIZZA PARAENSE', 'CAMARAO, JAMBU', 'PIZZAS', 34.90),
       ('PIZZA DE CALABRESA', 'CALABRESA', 'PIZZAS', 34.90),
       ('PIZZA DE MUSSARELA', 'MUSSARELA', 'PIZZAS', 34.90),
       ('PIZZA PORTUGUESA', 'MUSSARELA, PRESUNTO', 'PIZZAS', 34.90),
       ('COCA COLA', NULL, 'BEBIDAS', 7.90),
       ('SUCO DE LARANJA', NULL, 'BEBIDAS', 6.90);

-- -----------------------------------------------------
-- Order entity
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS ORDER_ITEM (
  ID            INT           NOT NULL PRIMARY KEY AUTO_INCREMENT,
  PRODUCT       INT           NOT NULL,
  QUANTITY      INT           NOT NULL,
  DELIVERY_ADDR VARCHAR(500),
  NOTES         VARCHAR(100),

  INDEX FK_ORDER_PRODUCT_IDX (PRODUCT),

  CONSTRAINT FK_ORDER_PRODUCT
    FOREIGN KEY (PRODUCT)
    REFERENCES PRODUCT (ID)
    ON DELETE NO ACTION ON UPDATE NO ACTION
);

INSERT INTO ORDER_ITEM (PRODUCT, QUANTITY, DELIVERY_ADDR, NOTES)
VALUES (1, 1, NULL, 'SEM CEBOLA'),
       (5, 1, NULL, NULL);

-- -----------------------------------------------------
-- Order History entity
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS ORDER_HISTORY (
  ID       INT NOT NULL,
  PRODUCT  INT NOT NULL,
  QUANTITY INT NOT NULL,

  INDEX FK_ORDER_HISTORY_PRODUCT_IDX (PRODUCT),

  CONSTRAINT FK_ORDER_HISTORY_PRODUCT 
      FOREIGN KEY (PRODUCT) REFERENCES PRODUCT (ID)
      ON DELETE NO ACTION ON UPDATE NO ACTION
);

INSERT INTO ORDER_HISTORY (ID, PRODUCT, QUANTITY)
VALUES (0, 1, 1), 
       (0, 5, 1),
       (0, 4, 1),
       (0, 6, 1);