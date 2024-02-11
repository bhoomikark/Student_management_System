package com.sms.student;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;

public class StudentMainPro
{
   public static void main(String[] args) throws ClassNotFoundException, SQLException
   {
	  intro();
	  Class.forName("com.mysql.cj.jdbc.Driver");
	  Scanner s1=new Scanner(System.in);
	  while(true) {
		  intro();
		  System.out.println("==============================================");
		  System.out.println("Choose the Operation: ");
		  int o=s1.nextInt();
		  switch (o) {
		case 1:
			System.out.println("**********************************************");
			System.out.println("**         ** INSERT RECORD**               **");
			System.out.println("**********************************************");
			insert();
			System.out.println("______________________________________________\n");
			
			break;
		case 2:
			System.out.println("**********************************************");
			System.out.println("**         ** EDIT RECORD**               **");
			System.out.println("**********************************************");
			edit();
			System.out.println("______________________________________________\n");
			
			break;
		case 3:
			System.out.println("**********************************************");
			System.out.println("**         ** VIEW RECORD**               **");
			System.out.println("**********************************************");
			view();
			System.out.println("______________________________________________\n");
			
			break;
		case 4:
			System.out.println("**********************************************");
			System.out.println("**         ** DELETE RECORD**               **");
			System.out.println("**********************************************");
			delete();
			System.out.println("______________________________________________\n");
		case 5:
			System.out.println("Program Stopped");
			System.exit(0);
			
			break;
			
			
			

		default:
			System.out.println("Enter the Valid Number");
			break;
		}
	  }
	  //insert();
	  
	  
   }
   public static void delete() throws ClassNotFoundException, SQLException{
	   String url="jdbc:mysql://localhost:3306/sms_db";
		  Connection con=DriverManager.getConnection(url, "root", "1234$bhoomika");
		  //edit();
		  //view();
		  String q="DELETE FROM student_info WHERE(id=?);";
		  PreparedStatement ps=con.prepareStatement(q);
		  Scanner s=new Scanner(System.in);
		  System.out.println("Select Id to Delet: ");
		  int id=s.nextInt();
		  ps.setInt(1, id);
		  ps.executeUpdate();
		  System.out.println("Record deleted successfully");
	   
   }
   public static void edit() throws ClassNotFoundException, SQLException{
	   String url3="jdbc:mysql://localhost:3306/sms_db";
		  Connection con3=DriverManager.getConnection(url3, "root", "1234$bhoomika");
		  view();
		  String query="UPDATE student_info SET Name = ?,std=?,fname=?,mobile=? WHERE(id=?);";
		  
		  PreparedStatement ps=con3.prepareStatement(query);
		  
		  Scanner s=new Scanner(System.in);
		  System.out.println("Select the id to EDIT: ");
		  int i=s.nextInt();
		  System.out.println("Enter Name: ");
		  s.nextLine();
		  String n=s.nextLine();
		  System.out.println("Enter STD: ");
		  String c=s.nextLine();
		  System.out.println("Enter Fname: ");
		  String fn=s.nextLine();
		  System.out.println("Enter Mobile: ");
		  String mob=s.nextLine();
		  
		  
		  ps.setString(1, n);
		  ps.setString(2, c);
		  ps.setString(3, fn);
		  ps.setString(4, mob);
		  ps.setInt(5,i);
		  ps.executeUpdate();
		  System.out.println("Data Updated Successfully");
		  
		  
   }
	  
   public static void view() throws SQLException {
	   String url1="jdbc:mysql://localhost:3306/sms_db";
		  Connection con1=DriverManager.getConnection(url1, "root", "1234$bhoomika");
	   Statement st=con1.createStatement();
		  ResultSet rs=st.executeQuery("select * from student_info");
		  System.out.println("ID | NAME | std | father | Mobile");
		  System.out.println("_____________________________________");
		  while(rs.next()) {
			  System.out.println(rs.getInt(1)+" | "+rs.getString(2)+" | "+rs.getString(3)+" | "+rs.getString(4)+" | ");
		  }
		  
		  
		  
		  
	   }
   
   public static void insert() throws SQLException {
	   Scanner s=new Scanner(System.in);
	   String url="jdbc:mysql://localhost:3306/sms_db";
		  Connection con=DriverManager.getConnection(url, "root", "1234$bhoomika");
		  System.out.println("Enter ur Name: ");
		  String n=s.nextLine();
		  System.out.println("Enter ur Class: ");
		  String c=s.nextLine();
		  System.out.println("Enter ur Father Name: ");
		  String f=s.nextLine();
		  System.out.println("Enter ur Mobile No: ");
		  String m=s.nextLine();
		  
		  
		  String query="insert into student_info(name,std,fname,mobile) " + "value(?,?,?,?)";
		  PreparedStatement ps=con.prepareStatement(query);
		  ps.setString(1, n);
		  ps.setString(2, c);
		  ps.setString(3, f);
		  ps.setString(4, m);
		  
		  
		  ps.executeUpdate();
		  System.out.println("data inserted successfully.....");
		  
		  
		  
	   
   }
   public static void intro() {
	   System.out.println("*******************");
	   System.out.println("* STUDENTS MODULE *");
	   System.out.println("********************");
	   System.out.println("\n 1.Insert");
	   System.out.println("2.Edit");
	   System.out.println("3.View");
	   System.out.println("4.Delete");
	   System.out.println("5.Stop");
   }
}
