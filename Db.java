import java.sql.DriverManager;
import java.sql.Connection;
import java.sql.SQLException;
import java.sql.ResultSet;
import java.sql.Statement;
import java.io.*;

public class Db {
static String s=null;
  public static void main(String[] argv) {

	System.out.println("-------- MySQL JDBC Connection Testing ------------");

	try {
		Class.forName("com.mysql.jdbc.Driver");
	} catch (ClassNotFoundException e) {
		System.out.println("Where is your MySQL JDBC Driver?");
		e.printStackTrace();
		return;
	}

	System.out.println("MySQL JDBC Driver Registered!");
	Connection connection = null;

	try {
		connection = DriverManager.getConnection("jdbc:mysql://www.db4free.net:3306/gpstrackerapp","aravinddbz", "tysontyson");

	} catch (SQLException e) {
		System.out.println("Connection Failed! Check output console");
		e.printStackTrace();
		return;
	}

	if (connection != null) {
		System.out.println("You made it, take control your database now!");
try{		
Statement st = connection.createStatement();
		ResultSet rs = st.executeQuery("SELECT * from location");
		while(rs.next())
            {
               String a= rs.getString("usid")+" "+rs.getString("lat")+" "+rs.getString("lon");
                System.out.println(a);
}
	try{
		Process p=Runtime.getRuntime().exec("uname -a");
		BufferedReader stdInput = new BufferedReader(new InputStreamReader(p.getInputStream()));
		  while ((s = stdInput.readLine()) != null) {
                System.out.println(s);
            }
}
catch(IOException e)
{
e.printStackTrace();
}
}
catch (SQLException e)
{
e.printStackTrace();
}
	} else {
		System.out.println("Failed to make connection!");
	}
  }
}
