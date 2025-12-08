const std = @import("std");
const print = std.debug.print;

pub fn main() !void {
    const file = try std.fs.cwd().openFile("./2019/day01/input.txt",.{});
    defer file.close();

    var file_buffer: [4096]u8 = undefined;
    var reader = file.reader(&file_buffer);
    var sum: i64 = 0;
    while (try reader.interface.takeDelimiter('\n')) |line| {
        const line_value = try std.fmt.parseInt(i64, line, 10);
        sum += @divFloor(line_value, 3) - 2;
    }
    print("{d}\n", .{sum});
}