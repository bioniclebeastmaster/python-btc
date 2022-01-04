/* 
Database: MySQL Ver 8.0.27
ddl statement for btcusdt_1m_klines table
*/
CREATE TABLE `btcusdt_1m_klines` (
  `open_time` datetime NOT NULL,
  `open` DECIMAL(13,2) NOT NULL,
  `high` DECIMAL(13,2) NOT NULL,
  `low` DECIMAL(13,2) NOT NULL,
  `close` DECIMAL(13,2) NOT NULL,
  `volume` DECIMAL(16,5) NOT NULL,
  `close_time` datetime NOT  NULL,
  `quote_asset_volume` DECIMAL(19,8) NOT NULL,
  `number_of_trades` bigint NOT NULL,
  `taker_buy_base_asset_volume` DECIMAL(16,5) NOT NULL,
  `taker_buy_quote_asset_volume` DECIMAL(19,8) NOT NULL,
  PRIMARY KEY (open_time) /* ensuring there is a primary key constraint */
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;