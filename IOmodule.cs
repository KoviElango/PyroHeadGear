using UnityEngine;
using System.Collections;
public class TestIO : {
    public UnityEngine.UI.Text text;
	// Use this for initialization
	void Start () {
        //File.Create("/mnt/sdcard/demo.txt");
        //File.Create("/storage/sdcard/demo.txt");
        if (File.Exists("/sdcard/test.txt"))
        {
            try
            {
                StreamReader fs = new StreamReader("/sdcard/test.txt", Encoding.Default);
            }
            catch (System.FileLoadException e)
            {
                text.text = e.Message;
            }
            //text.text = File.OpenText("/sdcard/test.txt").Read().ToString();
        }
    }
	// Update is called once per frame
	void Update () {
        //text.text = Application.persistentDataPath     
    }
}
