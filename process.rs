use std::io::{self, Read};

fn main() -> io::Result<()> {
    // let arg1 = std::env::args().nth(1).expect("no pattern given");
    // println!("{}", arg1);

    let mut buffer = String::new();
    io::stdin().read_to_string(&mut buffer)?;
 
    // println!("{}", buffer);

    for line in buffer.lines() {
        // println!("LINE {}", line);
        if line.starts_with("i(v1)") {
            println!("{}", &line[8..]);
        }
    }

    Ok(())
}