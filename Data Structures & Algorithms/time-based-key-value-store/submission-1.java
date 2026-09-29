class TimeMap {

    private java.util.Map<String, java.util.TreeMap<Integer, String>> map;

    public TimeMap() {
        map = new java.util.HashMap<>();
    }

    public void set(String key, String value, int timestamp) {
        map.putIfAbsent(key, new java.util.TreeMap<>());
        map.get(key).put(timestamp, value);
    }

    public String get(String key, int timestamp) {
        if (!map.containsKey(key)) {
            return "";
        }

        java.util.TreeMap<Integer, String> values = map.get(key);

        java.util.Map.Entry<Integer, String> entry =
            values.floorEntry(timestamp);

        if (entry == null) {
            return "";
        }

        return entry.getValue();
    }
}
