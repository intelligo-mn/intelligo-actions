export async function execute(command: string) {
  const exec = require("child_process").exec;
  await exec(command, (err: any, stdout: any, stderr: any) => {
    process.stdout.write(stdout);
  });
}
