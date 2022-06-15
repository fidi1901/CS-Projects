import java.util.*;

public class graderunner {
  public static void main(String[] args) {
    Course physics = new Course();
    physics.addAssignment("Assignment 1");
    physics.addStudent("idris034");
    physics.addStudent("fidi1901");
    physics.addStudent("abdisa10");
    physics.assignGrade("idris034", "Assignment 1", 100);
    physics.assignGrade("idris034", "Assignment 2", 97);
    physics.assignGrade("fidi1901", "Assignment 1", 95);
    physics.assignGrade("abdisa10", "Assignment 2", 37);
    for (String name : physics.hash.keySet()) {
      HashMap<String, Integer> value = physics.hash.get(name);
      System.out.println(name + " : " + value);
    }
    System.out.println(physics.getGradeAvg());
  }
}
