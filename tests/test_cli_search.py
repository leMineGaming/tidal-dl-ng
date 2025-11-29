"""Tests for CLI search functionality."""


from tidal_dl_ng.cli import SEARCH_TYPE_MAP, _format_duration, _init_search_type_map


class TestFormatDuration:
    """Tests for the _format_duration function."""

    def test_format_duration_positive(self):
        """Test formatting a positive duration."""
        assert _format_duration(90) == "01:30"

    def test_format_duration_zero(self):
        """Test formatting a zero duration."""
        assert _format_duration(0) == "00:00"

    def test_format_duration_negative(self):
        """Test formatting a negative duration returns empty string."""
        assert _format_duration(-1) == ""

    def test_format_duration_large(self):
        """Test formatting a large duration."""
        assert _format_duration(3661) == "61:01"


class TestSearchTypeMap:
    """Tests for the search type map initialization."""

    def test_init_search_type_map(self):
        """Test that _init_search_type_map populates the SEARCH_TYPE_MAP."""
        # Clear the map first
        SEARCH_TYPE_MAP.clear()

        # Initialize it
        _init_search_type_map()

        # Verify the expected keys exist
        expected_keys = ["track", "album", "artist", "video", "playlist"]
        for key in expected_keys:
            assert key in SEARCH_TYPE_MAP

    def test_search_type_map_values_are_classes(self):
        """Test that search type map values are class types."""
        _init_search_type_map()

        for key, value in SEARCH_TYPE_MAP.items():
            assert isinstance(value, type), f"Expected type for key '{key}', got {type(value)}"
