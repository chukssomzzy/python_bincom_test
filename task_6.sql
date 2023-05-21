--save colours and their frequencies in postgresql db 

CREATE TABLE IF NOT EXIST color_distribution (
  color, VARCHAR NOT NULL, 
  freq, VARCHAR NOT NULL
);

INSERT INTO color_distribution (color, freq) 
VALUES 
  ('GREEN', 10), ('YELLOW', 5), ('BROWN', 6),
  ('BLUE', 31), ('PINK', 5), ('ORANGE', 9),
  ('CREAM', 2), ('RED', 9), ('WHITE', 16),
  ('ARSH', 1), ('BLACK', 1); 

-- show success
SELECT * FROM color_distribution
