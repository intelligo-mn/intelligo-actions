import { execute } from "../src/execute";

test("install package", async () => {
  await expect(execute("intelligo")).rejects.toThrow(
    "not install test package"
  );
});
