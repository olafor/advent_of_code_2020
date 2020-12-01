
fn main() {
    let mut answer = 42;
    let test:bool = false;
    let char_test:char = 's';

    assert_eq!(answer, 42);

    answer = 31;

    
    println!("Hello {}", answer);
    println!("It i{} {}!", char_test, !test);
}
