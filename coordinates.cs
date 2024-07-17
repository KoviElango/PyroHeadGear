
    public class Coordinates :  {
    double absoluteGPSUser1Lat, absoluteGPSUser1Lon, absoluteGPSUser2Lat,        absoluteGPSUser2Lon;
    Transform absoluteUserpos1, absoluteUserpos2;
    void Start () {
        relativeUserpos1.Set(0, 0);
        absoluteGPSUser1Lat=13.111936;
        absoluteGPSUser2Lat=13.031;
        absoluteGPSUser1Lat = (absoluteUser1Lat - 13) * 10000;
        relativeUserpos2.Set((float)absoluteGPSUser2Lat - (float)absoluteGPSUser1Lat, 0f);        
    }
