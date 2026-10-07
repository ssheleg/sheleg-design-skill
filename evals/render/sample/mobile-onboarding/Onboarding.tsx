export function Onboarding() {
  const steps = [
    { title: "Add a plant", icon: "🌱" },
    { title: "Set a reminder", icon: "⏰" },
  ];
  return (
    <section className="bg-gradient-to-r from-indigo-500 to-purple-600 onboarding">
      {steps.map((s) => (
        <div key={s.title} className="step">{s.title}</div>
      ))}
    </section>
  );
}
