"""
Tests for data ingestion sync manager.
"""
import pytest
from src.ingestion.sync import DataSyncManager

def test_data_sync_manager_init() -> None:
    sync_manager = DataSyncManager(db_config={"provider": "firestore"})
    assert sync_manager.db_config["provider"] == "firestore"

def test_sync_records_count() -> None:
    sync_manager = DataSyncManager(db_config={})
    records = [{"temp": 22.0}, {"temp": 24.5}]
    count = sync_manager.sync_records(records)
    assert count == 2
