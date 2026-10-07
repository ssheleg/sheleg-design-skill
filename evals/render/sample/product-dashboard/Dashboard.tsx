export function Dashboard({ tickets }: { tickets: { id: string; age: number }[] }) {
  return (
    <table className="tickets">
      <tbody>
        {tickets.map((t) => (
          <tr key={t.id}>
            <td className="text-zinc-500" style={{ color: "#333" }}>{t.id}</td>
            <td>{t.age}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
