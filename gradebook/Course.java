import java.util.*;
public class Course{
  HashMap<String, HashMap<String, Integer>> hash;
  List<String> assignments;
  List<String> students;
  public Course(){
    assignments = new ArrayList<>();
    students = new ArrayList<>();
    hash = new HashMap<>();
  }
  public boolean isIn(String id, List<String> ls){
    for(int i = 0; i<ls.size(); i++){
      if(ls.get(i) == id){
        return true;
      }
    }
    return false;
  }
  public void addAssignment(String assignmentId){
    if(isIn(assignmentId, assignments)){
      System.out.println("error1");
    }
    else{
      assignments.add(assignmentId);
    }
  }
  public void addStudent(String studentId){
    if(isIn(studentId, students)){
      System.out.println("error2");
    }
    else{
      students.add(studentId);
      hash.put(studentId, new HashMap<String, Integer>());
    }
  }
  public void assignGrade(String studentId, String assignmentId, int grade){
    HashMap<String, Integer> gradeb = hash.get(studentId);
    gradeb.put(assignmentId, grade);
  }
  public float getGradeAvg(){
    int counter = 0;
    int avg = 0;
    for(String key : hash.keySet()){
      HashMap<String, Integer> grades = hash.get(key);
      for(String key2: grades.keySet()){
        counter++;
        avg+= grades.get(key2);
      }
    }
    float ret = (float) (avg / counter);
    return ret;
  }

}
