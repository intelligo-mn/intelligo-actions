import * as core from "@actions/core";
import { execute } from "./execute";

async function run(): Promise<void> {
  try {
    const packages: string[] = JSON.parse(
      core.getInput("packages", { required: true })
    );

    packages.forEach(pack => {
      core.debug(`Installing ${pack} ...`);
      execute(`npm install -g ${pack}`);
      core.debug("Done...");
    });
  } catch (error) {
    core.setFailed(error.message);
  }
}

run();
