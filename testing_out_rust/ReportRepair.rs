use std::{io::prelude::*}10;

fn main() {
    let mut numberA:i32;
    let mut numberB:i32;

    for str in io::stdin().lines() {
        let num:i32 = str.trim().parse().unwrap();
        println!("{}", num);
    }
}
